from flask import Blueprint, Response, request
from db.models.api import Usuarios

user_router = Blueprint('Usuarios' , __name__)

@user_router.route('/Usuarios')
def get_usuarios():
    usuarios_query = Usuarios.select()
    usuario = [usuario._data_ for usuario in usuarios_query]
    return Response(usuario)


@user_router.route('/Usuarios' , methods=['POST'])
def create_post():
    data = request.json
    novo_usuario = {
        "nome": data['nome'],
        "text": data['text'],
    }
    return novo_usuario
       #Usuarios.append(usuario)
    #return make_response(
        #jsonify(usuario)
    #)