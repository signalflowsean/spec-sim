# ---- THIRD PARTY IMPORTS ---- 
# pylint: disable=F0401
from flask import Flask

# ---- FIRST PARTY IMPORTS ---- 
from routes.deeplearner.route import deeplearner_blueprint

# ---- CONSTANTS ----
UPLOAD_FOLDER = './files'

# ---- INITIALIZE FLASK APP ----
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register routes
app.register_blueprint(deeplearner_blueprint)

if __name__ == "__main__":
  app.run()