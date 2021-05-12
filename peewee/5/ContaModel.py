from peewee import *

db = SqliteDatabase('conta.db')


class BaseModel(Model):
    class Meta:
        database = db


class Conta(BaseModel):
    numero = CharField()
    agencia = CharField()
    saldo = FloatField()
    tipoConta = CharField()
    tipo = IntegerField()


class ContaBancaria(BaseModel):
    conta = ForeignKeyField(Conta, backref='conta')


class ContaImposto(BaseModel):
    conta = ForeignKeyField(Conta, backref='conta')
    percentualImposto = FloatField()


db.connect()
db.create_tables([Conta, ContaBancaria, ContaImposto])
