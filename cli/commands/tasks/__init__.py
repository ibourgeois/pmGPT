""" Tasks commands. """
import typer

from .show import show_task
from .list import list_tasks
from .create import new_task

app = typer.Typer()

app.command(name="list", help="List tasks.     Usage: tasks list")(list_tasks)
app.command(name="new",  help="Add a new task. Usage: tasks add <task_description>")(new_task)
app.command(name="show", help="Show a task.    Usage: tasks show <task_id>")(show_task)
