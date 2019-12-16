# ---- THIRD PARTY IMPORTS ----
# pylint: disable=F0401
from flask import Blueprint
from flask import request

# ---- FIRST PARTY IMPORTS ----
# pylint: disable=E0611
from utils import umap

deeplearner_blueprint = Blueprint('deeplearner', __name__)

# ---- ROUTES ----
# Hit this endpoint to test connection with the deep-learner api
@deeplearner_blueprint.route('/')
def testConnection():
  return umap.test()

# Hit this endpoint to compute umap features
@deeplearner_blueprint.route('/features', methods = ['POST', 'GET'])
def postFeatures(): 
  if request.method == 'GET':
    return umap.computeFeatures()