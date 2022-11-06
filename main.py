import pandas as pd
from peewee import *

from models.prof import prof
from models.ra import ra
from models.registration import registration
from models.student import student

#db = SqliteDatabase("database.db")
#query = prof.select().join(ra)

#raprof = int(input("Digite o RA do professor desejado: "))



#newquery = ra.select().where( ra.prof_id == raprof ).count()
#print(f"quantidade de alunos do Professor de RA {raprof} é: {newquery}")

profs = prof.select()

for professor in profs:
        students_count = ra.select().where(ra.prof_id == professor.prof_id).count()
        print(f"O professor {professor.prof_id} tem {students_count} alunos e tem a capacidade de ensino de {professor.teachingability}")



#print(df.loc[0])

#db.loc[] pegar primeira celula