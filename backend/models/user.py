from flask import Blueprint, jsonify, request
from peewee import *
import datetime
  


database = SqliteDatabase('sever.db')

class User(Model):
    nome = CharField()
    text = TextField()
    data = DateTimeField(default=datetime.datetime.now)


    class Meta:
        database = database

    def serialize(self):
        return{
            'nome' : self.nome,
            'text' : self.text,
        }


database.connect()
database.create_tables([User])

# ~~~~~~~~~~~~ fim da api  ~~~~~~~~~~~~~~~


user_routes = Blueprint('user', __name__)


@user_routes.route('/user', methods=['GET'])
def listar():
    users = User.select()
    return jsonify([user.serialize() for user in users])


@user_routes.route('/user', methods={'POST'})
def inserir():
    data = request.get_json

    new = User.create(
        nome = data['nome'], text = data['text']
    )

    return jsonify(new.serialize())