from flask import Flask, jsonify, request
from peewee import *
import datetime

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

# ~~~~~~~~~~~~  xxxxxx ~~~~~~~~~~~~~~~

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá"

@app.route('/users', methods=['GET'])
def listar():
    users = User.select()
    return jsonify([user.MyJson() for user in users ])


@app.route('/users', methods={'POST'})
def inserir():
    data = request.get_json

    new = User.create(
        nome = data['nome'], text = data['text']
    )

    return jsonify(new)

if __name__ == '__main__':
    app.run(debug=True)