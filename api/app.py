# ---- THIRD PARTY IMPORTS ---- 
# pylint: disable=F0401
from flask import Flask
from flask_cors import CORS

# ---- FIRST PARTY IMPORTS ---- 
from routes.deeplearner.route import deeplearner_blueprint
from routes.dbhelper.route import dbhelper_blueprint
from routes.audiolibrary.route import audiolibrary_blueprint

# ---- CONSTANTS ----
UPLOAD_FOLDER = './uploaded_files_to_s3'

# ---- INITIALIZE FLASK APP ----
app = Flask(__name__)

# Initialize CORS with the flask application
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register blueprints
app.register_blueprint(deeplearner_blueprint)
app.register_blueprint(dbhelper_blueprint)
app.register_blueprint(audiolibrary_blueprint)

# RUN THE THING!
if __name__ == "__main__":
  app.run()