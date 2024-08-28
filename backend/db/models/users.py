from peewee import Model, CharField, TextField, DateTimeField 
from db.database import db
import datetime

class User(Model):
    nome = CharField()
    post = TextField()
    date_Time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db