from enum import Enum

from fastapi import FastAPI

from models.prof import prof
from models.ra import ra
from models.registration import registration
from models.course import course as cs
from models.student import student

app = FastAPI()

class ModelName(str, Enum):
    dec = "descendente"
    cres = "ascendente"


@app.get("/students/{notas}")
async def root(notas: ModelName):
    courses = cs.select()
    yay = {}
    if notas is ModelName.cres:
        for course in courses:
            regs = registration.select().join(student).where(registration.course_id == course.courseId).order_by(registration.grade.asc())
            if len(regs) > 0:
                yay[str(course.courseId)] = []
                for reg in regs:
                    yay[str(course.courseId)].append(reg)

    if notas is ModelName.dec:
        for course in courses:
            regs = registration.select().join(student).where(registration.course_id == course.courseId).order_by(registration.grade.desc())
            if len(regs) > 0:
                yay[str(course.courseId)] = []
                for reg in regs:
                    yay[str(course.courseId)].append(reg)
    return yay

@app.get("/relatorio/aluno")
async def sla():
        registrations = registration.select().join(student).limit(5).order_by(student.ranking.desc())

        return {registrations[i] for i in range(len(registrations))}

@app.get("/relatorio/professor")
async def sla2():
        profs = prof.select().limit().order_by(prof.popularity.desc())

        return {profs[i] for i in range(len(profs))}

@app.get("/relatorio/curso")
async def sla3():
    courses = cs.select()

    cursos = {}
    for course in courses:
        regs_count = registration.select().where(registration.course_id == course.courseId).count()
        if regs_count > 0:
            cursos[str(course.courseId)] = {"quant": regs_count}
    return cursos
