from flask import jsonify, Blueprint, request
from peewee import DateTimeField, TextField, CharField, SqliteDatabase, Model
import datetime

db = SqliteDatabase('sever.db')

class User(Model):
    nome = CharField()
    text = TextField()
    time = DateTimeField(default= datetime.datetime.now)

    class Meta:
        database = db

    def MyJson(self):
        return{
            'nome' : self.nome,
            'text' : self.text
        }

db.connect()
db.create_tables([User])

# ~~~~~~~~~~~~~~~X~~~~~~~~~~~~~~~~

user_routes = Blueprint('user', __name__)

@user_routes.route('/', methods=['GET'])
def listar():
    users = User.select()
    return jsonify([user.MyJson() for user in users])

@user_routes.route('/', methods=['POST'])
def inserir():
    data = request.get_json

    new = User.create(
        nome = data['nome'], text = data['text']
    )

    return jsonify(new.MyJson)