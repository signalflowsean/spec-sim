# ---- THIRD PARTY IMPORTS ---- 
# pylint: disable=F0401
from flask import Flask
from flask_cors import CORS
import json


# ---- FIRST PARTY IMPORTS ---- 
from routes.deeplearner.route import deeplearner_blueprint
from routes.dbhelper.route import dbhelper_blueprint

# ---- CONSTANTS ----
UPLOAD_FOLDER = './uploaded_files_to_s3'

# ---- INITIALIZE FLASK APP ----
app = Flask(__name__)

# Initialize CORS with the flask application
CORS(app)

# logging.getLogger('flask_cors').level = logging.DEBUG

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register blueprints
app.register_blueprint(deeplearner_blueprint)
app.register_blueprint(dbhelper_blueprint)

if __name__ == "__main__":
  app.run()