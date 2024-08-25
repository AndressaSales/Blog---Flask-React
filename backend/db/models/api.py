from peewee import  Model, CharField, TextField, DateTimeField
from db.dataBase import db 
import datetime

class Usuarios(Model):
    #charField = varChar que vale até 250 caracters
    # unique = controla que não teja usuraios com o mesmo nome
    # TextFild = texto infinito
    nome = CharField(unique=True)
    text_conteudo = TextField() 
    data_time = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db