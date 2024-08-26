from flask import Blueprint, render_template
# importação da api
from db.user import USUARIOS

# Blueprint -> é um comando para agrupador de rotas
user_route = Blueprint('user', __name__)

# para o post pronto
@user_route.route('/')
def lista_user():
   title = 'Publicações'
   return render_template('lista.html', title=title, users=USUARIOS)

# para postagem
@user_route.route('/new')
def form_user():
    return render_template('index.html')


# inserir dados do poster no banco de dados
@user_route.route('/', methods=['POST'])
def inserir_user():
    pass

# exibir detalhes de um usuario
@user_route.route('/<int:user_id>')
def detalhe_user(user_id):
    return render_template()