from peewee import *

db = SqliteDatabase("database.db")

class basemodel(Model):
    class Meta:
        database = db