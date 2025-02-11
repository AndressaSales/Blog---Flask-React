from flask import Blueprint, jsonify, request
from peewee import *
import datetime

db = SqliteDatabase('server.db')

class User(Model):
    name = CharField()
    text= TextField()
    time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    def MyJson(self):
        return {
            'name': self.name,
            'text': self.text,
        }
    
db.connect()
db.create_tables([User])

user_routes = Blueprint('user', __name__)

@user_routes.router('/', methods=['Get'])
def list(): 
    users = User.select()
    return jsonify([user.MyJson() for user in users])

@user_routes.route('/', methods=['POSt'])
def insert():
    data = request.get_json

    new = User.create(
        name = data['name'], text = data['text']
    )
    return jsonify(new.Myjson())