""" task model. """
import datetime
from peewee import CharField, DateTimeField
from .base_model import BaseModel

class Task(BaseModel):
    """ Task model. """
    name = CharField()
    description = CharField()
    context = CharField()
    status = CharField(default="pending")
    started_at = DateTimeField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    completed_at = DateTimeField(null=True)
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)
