from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfsdfsdf'

    



    from .views import views
    #from .solar import solar
    #from .water import water

    app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')

    return app