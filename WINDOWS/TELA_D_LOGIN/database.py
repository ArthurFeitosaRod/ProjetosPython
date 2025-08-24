from peewee import *
import os

Diretorio_principal = os.path.dirname(__file__)
Diretorio_Log = os.path.join(Diretorio_principal, "LOG")
db = SqliteDatabase(os.path.join(Diretorio_Log, 'Login.db'))
class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    class Meta:
        database = db