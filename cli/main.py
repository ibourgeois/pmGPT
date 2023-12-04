""" Main entry point for the CLI. """
import typer
from cli.commands.setup import init
from cli.commands.tasks import app as tasks

app = typer.Typer()

app.command()(init)
app.add_typer(tasks, name="task", help="Manage tasks")

if __name__ == "__main__":
    app()
