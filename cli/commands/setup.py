""" The Init command. """
import os
import typer
from peewee import SqliteDatabase
from models._database import initialize_db
from config import settings

app = typer.Typer()

@app.command()
def init():
    """ 
    Initialize the database and create the tables.
    """
    if check_database_initialized():  # Implement this function
        typer.echo("Database is already initialized.")
        return
    initialize_db()
    typer.echo("Initialized the database.")

def check_database_initialized():
    """
    Check if the database is already initialized.
    """
    # Check if the database file exists
    if os.path.exists(settings.DATABASE_PATH):
        db = SqliteDatabase(settings.DATABASE_PATH)
        db.connect()
        # Check if the tables exist
        if not db.table_exists("tasks"):
            db.close()
            return False
        db.close()
        return True
    return False
