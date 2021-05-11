from peewee import *
import datetime


db = SqliteDatabase('urna.db')


class BaseModel(Model):
    class Meta:
        database = db


class Partido(BaseModel):
    numero = CharField()
    nome = CharField()


class Candidato(BaseModel):
    nome = CharField()
    partido = ForeignKeyField(Partido, backref='partido')
    zona = CharField()
    secao = CharField()


class Eleitor(BaseModel):
    nome = CharField()
    tituloEleitor = CharField()


class Voto(BaseModel):
    data = DateTimeField()
    candidato = ForeignKeyField(Candidato, backref='candidato')
    eleitor = ForeignKeyField(Eleitor, backref='eleitor')


# db.connect()
# db.create_tables([Candidato, Eleitor, Partido, Voto, UrnaEletronica])
