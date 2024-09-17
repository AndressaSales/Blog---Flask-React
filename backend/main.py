from flask import Flask
from flask_cors import CORS
# importaçõa da pag models/user
from user import user_routes

app = Flask(__name__)
CORS(app)
app.register_blueprint(user_routes, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)