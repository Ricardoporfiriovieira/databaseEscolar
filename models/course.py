from peewee import *

from models.base import basemodel


class course(basemodel):
    courseId = IntegerField(primary_key=True)
    rating = IntegerField()
    diff = IntegerField()
