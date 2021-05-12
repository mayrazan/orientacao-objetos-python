from peewee import *

db = SqliteDatabase('elevador.db')


class BaseModel(Model):
    class Meta:
        database = db


class ElevadorInfo(BaseModel):
    andarAtual = IntegerField()
    capacidade = IntegerField()
    quantidadePessoas = IntegerField()
    totalAndares = IntegerField()


db.connect()
db.create_tables([ElevadorInfo])
