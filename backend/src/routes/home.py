from flask import Blueprint

home = Blueprint('Home', __name__)


@home.route('/')
def home_pag():
    return "Olá, Mundo!"