from peewee import *

db = SqliteDatabase('bomba.db')


class BaseModel(Model):
    class Meta:
        database = db


class Bomba(BaseModel):
    tipoCombustivel = CharField()
    valorLitro = FloatField()
    quantidadeCombustivel = FloatField()


db.connect()
db.create_tables([Bomba])
