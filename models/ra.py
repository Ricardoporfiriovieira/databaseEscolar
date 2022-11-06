from peewee import *

from models.prof import prof
from models.student import student
from models.base import basemodel



class ra(basemodel):
    capabilty = CharField()
    prof_id = ForeignKeyField(prof)
    student_id = ForeignKeyField(student)
    salary = CharField()
