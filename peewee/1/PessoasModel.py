from peewee import *

db = SqliteDatabase('pessoas.db')


class BaseModel(Model):
    class Meta:
        database = db


class PessoasModel(BaseModel):
    nome = CharField()
    idade = IntegerField()
    peso = IntegerField()
    altura = FloatField()


db.connect()
db.create_tables([PessoasModel])
