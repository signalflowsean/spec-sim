# ---- THIRD PARTY IMPORTS ---- 
# pylint: disable=F0401
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import logging

# ---- FIRST PARTY IMPORTS ---- 
from config import Config
# from models import User, View

# ---- INITIALIZE THIRD PARTY LIBRARIES ----
db = SQLAlchemy()
migrate = Migrate()

cors = CORS()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  cors.init_app(app)

  db.init_app(app)
  migrate.init_app(app, db)

  return app