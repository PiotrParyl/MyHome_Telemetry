from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfsdfsdf'

    from .pump import pump
    from .solar import solar
    from .water import water

    app.register_blueprint(, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app