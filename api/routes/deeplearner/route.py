# ---- THIRD PARTY IMPORTS ----
import os

# pylint: disable=F0401
from flask import Blueprint
from flask import request

# ---- FIRST PARTY IMPORTS ----
# pylint: disable=E0611
from utils import umap, s3

deeplearner_blueprint = Blueprint('deeplearner', __name__)

# ---- ROUTES ----
# Hit this endpoint to test connection with the deep-learner api
@deeplearner_blueprint.route('/')
def testConnection():
  return umap.test()

# Hit this endpoint to add audio library
# Currently, only prints out the name of files in a bucket
@deeplearner_blueprint.route('/audiolibrary')
def printAudioLibraryInfo(): 
  # A bucketname of a bucket on s3
  bucketname = 'audio-library-02ee2898-212d-11ea-9a8c-0242c0a85002'
  return '\n'.join(s3.getAllFilesNamesInABucket(bucketname))

# Hit this endpoint to compute umap features
@deeplearner_blueprint.route('/features', methods = ['POST', 'GET'])
def postFeatures(): 
  if request.method == 'GET':
    return umap.computeFeatures()