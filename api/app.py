# ---- THIRD PARTY IMPORTS ---- 
# pylint: disable=F0401
from flask import Flask
from flask_cors import CORS

# ---- FIRST PARTY IMPORTS ---- 
from routes.deeplearner.route import deeplearner_blueprint

# ---- CONSTANTS ----
UPLOAD_FOLDER = './uploaded_files_to_s3'

# ---- INITIALIZE FLASK APP ----
app = Flask(__name__)
CORS(app)

# logging.getLogger('flask_cors').level = logging.DEBUG

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register routes
app.register_blueprint(deeplearner_blueprint)

if __name__ == "__main__":
  app.run()