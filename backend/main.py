from flask import Flask
from routes.user import user_route

app = Flask(__name__)

# Blueprint -> é um comando para agrupador de rotas
@app.register_blueprint(user_route)

app.run(debug=True)