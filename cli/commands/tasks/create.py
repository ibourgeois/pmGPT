""" Create a new task. """
import json
import typer
import openai
from openai import OpenAI
from config import settings
from models.task import Task

app = typer.Typer()

@app.command()
def new_task(description: str):
    """
    Create a new task.
    """
    print("Expanding task description with OpenAI API...")
    description = expand_task_description(description)
    tasks = json.loads(description)['tasks']
    for task in tasks:
        task = Task(
            name=task['name'],
            description=task['description'],
            context=task['context'],
        )
        task.save()
        typer.echo(f"Task created: {task.name}")

def expand_task_description(description: str):
    """
    Expand task description with OpenAI API.
    """
    client = OpenAI(
        api_key=settings.OPENAI_API_KEY,
    )
    try:
        # Make the API call to OpenAI's completion endpoint
        response = client.chat.completions.create(
            messages = [{
                "role": "user", 
                "content": generate_prompt(description),
            }],
            model = "gpt-4-1106-preview",
            response_format = {"type": "json_object"}
        )

        # Extract the story from the response
        expanded_task = response.choices[0].message.content
        return expanded_task
    except openai.APIConnectionError as e:
        print("The server could not be reached")
        print(str(e.__cause__))
        return None
    except openai.RateLimitError:
        print("A 429 status code was received; we should back off a bit.")
        return None
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)
        return None

def generate_prompt(description: str):
    """ Generate a prompt for the OpenAI API."""
    return (
        "You are a helpful and eager Project Manager that accepts " 
        "simple task descriptions from a Software Developer and can "
        "determine if the task can be broken down into smaller tasks, "
        "or if it can be just one task. Then you return an expanded "
        "version of each task in json format that includes best agile "
        "practices. Such as, including 'context, 'acceptance_criteria' "
        "and any other information relevant to completing the task.\n\n"
        "Use the following format:\n\n"
        "{\n"
        "    \"tasks\": [\n"
        "        {\n"
        "            \"name\": \"\",\n"
        "            \"description\": \"\",\n"
        "            \"context\": \"\",\n"
        "            \"acceptance_criteria\": []\n"
        "        }\n"
        "    ]\n"
        "}\n"
        f"Task description: {description}"
    )
