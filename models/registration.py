from peewee import *

from models.student import student
from models.base import basemodel
from models.course import course


class registration(basemodel):
    course_id = ForeignKeyField(course)
    student_id = ForeignKeyField(student)
    grade = CharField()
    sat = CharField()
