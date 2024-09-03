from flask import Blueprint, request, jsonify
from db.models.users import User

# Blueprint -> é um comando para agrupador de rotas
user_route = Blueprint('usuario', __name__)

# rota para listar todos os usuarios
@user_route.route('/user', methods=['GET'])
def lista_user():
    user = User.select()
    return jsonify(user)
   
# rota paracriar um novo usuario
@user_route.route('/user', methods=['POST'])
def create_user():
    data = request.json

    new_user =  User.create(
        nome = data['nome'],
        post = data['post']
    )
    return jsonify({ 'nome': new_user.nome, 'post': new_user.post})