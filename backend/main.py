from flask import Flask

# importaçõa da pag models/user
from models.user import user_routes

app = Flask(__name__)

app.register_blueprint(user_routes, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)