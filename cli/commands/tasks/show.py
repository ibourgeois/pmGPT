""" Show a task. """
import typer
from models.task import Task

app = typer.Typer()

@app.command()
def show_task(task_id: int):
    """
    Show a task.
    """
    task = Task.get_by_id(task_id)
    typer.echo(
        "----------------------------------------\n"
        f"{task.id}: {task.name} - {task.status}\n"
        "----------------------------------------\n"
        "Description:\n"
        f"{task.description}\n\n"
        "Context:\n"
        f"{task.context}\n"
        "----------------------------------------\n"
    )
