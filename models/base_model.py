""" Base model for all other models. """
from peewee import Model
from ._database import db

class BaseModel(Model):
    """ Base model for all other models. """
    class Meta:
        """ Meta class for the base model. """
        database = db
