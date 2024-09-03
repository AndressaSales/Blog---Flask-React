from flask import Flask
# importação do configuração
from routes.user import user_route
from db.database import db
from db.models.users import User

app = Flask(__name__)

# register_blueprin -> é usada para associar um Blueprint á aplicação flask principal
app.register_blueprint(user_route)

def config_rotas():
    # inicializar o banco de dados
    db.connect()
    db.create_tables([User])
 

app.run(debug=True)