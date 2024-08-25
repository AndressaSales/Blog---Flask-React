from flask import Blueprint, render_template
# Blueprint -> é um comando para agrupador de rotas

user_route = Blueprint('user', __name__)

@user_route.route('/')
def user():
    return render_template('index.html')