from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import logging
from logging.handlers import RotatingFileHandler
import os

App = Flask(__name__)
App.config.from_object(Config)
db = SQLAlchemy(App)
migrate = Migrate(App, db)
login = LoginManager(App)
login.login_view = 'login'

from app import routes, models, errors

if not App.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes = 10240, backupCount = 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s : %(message)s [in %(pathname)s: %(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    App.logger.addHandler(file_handler)

    App.logger.setLevel(logging.INFO)
    App.logger.info('Microblog startup')
