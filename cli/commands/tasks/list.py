""" List all tasks. """
import typer
from models.task import Task

app = typer.Typer()

@app.command()
def list_tasks():
    """
    List all tasks.
    """
    tasks = Task.select()
    for task in tasks:
        typer.echo(f"{task.id}: {task.name} - {task.status}")
