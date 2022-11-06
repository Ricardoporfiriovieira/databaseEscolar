from peewee import *

from models.base import basemodel


class student(basemodel):
    student_id = IntegerField(primary_key=True)
    inteligence = CharField()
    ranking = CharField()
