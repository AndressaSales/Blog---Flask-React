from flask import Blueprint, jsonify, request
from peewee import *
import datetime
  
# conexão de banco de dados aprimorada (assumindo o SQLite )
database = SqliteDatabase('sever.db')

class User(Model):
    nome = CharField()
    text = TextField()
    data = DateTimeField(default=datetime.datetime.now)


    class Meta:
        database = database

    def MyJson(self):
        return{
            'nome' : self.nome,
            'text': self.text
        }


database.connect() 
database.create_tables([User])

u = User(nome = "jcbakjcbjdcb", text= "ckjdbckdsjcbd")
u.save()

# ~~~~~~~~~~~~  xxxxxx ~~~~~~~~~~~~~~~


user_routes = Blueprint('user', __name__)


@user_routes.route('/', methods=['GET'])
def listar():
    users = User.select()
    return jsonify([user.MyJson() for user in users ])


@user_routes.route('/', methods={'POST'})
def inserir():
    data = request.get_json

    new = User.create(
        nome = data['nome'], text = data['text']
    )

    return jsonify(new)