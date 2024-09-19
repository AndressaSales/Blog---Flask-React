from flask import Flask
from models.user import user_routes
from routes.home import home

app= Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(user_routes, url_prefix="/user")

if __name__ == '__main__':
    app.run(debug=True)