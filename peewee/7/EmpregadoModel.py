from peewee import *

db = SqliteDatabase('empregado.db')


class BaseModel(Model):
    class Meta:
        database = db


class EmpregadoInfo(BaseModel):
    nome = CharField()
    sobrenome = CharField()
    salarioMensal = FloatField()
    aumentoSalario = FloatField()


db.connect()
db.create_tables([EmpregadoInfo])
