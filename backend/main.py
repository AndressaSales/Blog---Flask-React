from flask import Flask, jsonify
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

user = User(nome = 'Alex', text = 'Ola')
user.save()

database.close()
app = Flask(__name__)

@app.route('/user', methods=['GET'])
def listar():
    user = User.select()
    return jsonify([user.serialize()])

if __name__ == '__main__':
    app.run(debug=True)