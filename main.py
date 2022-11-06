import pandas as pd
from peewee import *

from models.prof import prof
from models.ra import ra
from models.student import student

#db = SqliteDatabase("database.db")
query = prof.select().join(ra)   

newquery = ra.select().where( ra.prof_id == 6 ).count()
print(f"quantidade de alunos desse Professor: {newquery}")





#print(df.loc[0])
#db.loc[] pegar primeira celula