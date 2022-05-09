from werkzeug import secure_filename,FileStorage
from flask_bootstrap import Bootstrap
from config import config_options
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

login_manager=LoginManager()
login_manager.session='strong'
login_manager.login_view='auth.login'

bootstrap=Bootstrap()
db=SQLAlchemy()
photos=UploadSet('photos',IMAGES)
mail=Mail()

def create_app(config_name):
    #create flask app instance
    app=Flask(__name__)

    app.config.from_object(config_options[config_name])

    configure_uploads(app,photos)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    return app