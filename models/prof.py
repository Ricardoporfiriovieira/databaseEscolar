from peewee import *


from models.base import basemodel



class prof(basemodel):
    prof_id = IntegerField(primary_key=True)
    popularity = CharField()
    teachingability = CharField()

