from flask import Flask
from models.user import user_routes

app = Flask(__name__)

@app.router('/')
def Home():
    return 'Olá, Mundo'

app.register_blueprint(user_routes, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True)