from routes.user import user_route

def config_all(app):
    config_rotas(app)

def config_rotas(app):
    # register_blueprin -> é usada para associar um Blueprint á aplicação flask principal
    app.register_blueprint(user_route,  url_prefix='/user')
    