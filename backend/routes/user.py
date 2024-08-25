from flask import  Flash, request,  Response, render_template
from db.models.api import Usuarios

app = Flash(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Usuarios')
def get_usuarios():
    usuarios_query = Usuarios.select()
    usuario = [usuario._data_ for usuario in usuarios_query]
    return Response(usuario)


@app.route('/Usuarios' , methods=['POST'])
def create_post():
    data = request.json
    novo_usuario = {
        "nome": data['nome'],
        "text": data['text'],
    }

    Usuarios.append(novo_usuario)
    return render_template('index.html', usuario=novo_usuario)

       #Usuarios.append(usuario)
    #return make_response(
        #jsonify(usuario)
    #)