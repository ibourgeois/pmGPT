""" Database connection. """
from peewee import SqliteDatabase

from config import settings

db = SqliteDatabase(settings.DATABASE_PATH)

def initialize_db():
    """ Connect to the database. """
    db.connect()
    from .task import Task
    db.create_tables([Task], safe=True)
