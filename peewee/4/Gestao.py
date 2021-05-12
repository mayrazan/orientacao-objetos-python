from peewee import *

db = SqliteDatabase('gestao.db')


class BaseModel(Model):
    class Meta:
        database = db


class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    cpf = CharField()


class Funcionario(BaseModel):
    pessoa = ForeignKeyField(Pessoa, backref='pessoa')
    salario = FloatField()


class Empresa(BaseModel):
    nome = CharField()
    funcionario = ForeignKeyField(Funcionario, backref='funcionario')


db.connect()
db.create_tables([Pessoa, Funcionario, Empresa])
