# ---- THIRD PARTY IMPORTS ----
import os
# pylint: disable=F0401
from flask import Blueprint, request, make_response

# ---- FIRST PARTY IMPORTS ----
# pylint: disable=E0611
from utils import umap, s3, df, files as fs, df

# ---- CONSTANTS ----
foldername = 'downloaded_files_from_s3'
downloadPath = './%s' % (foldername)

# Register flask blueprint
deeplearner_blueprint = Blueprint('deeplearner', __name__)

# ---- ROUTES ----
# Hit this endpoint to test connection with the deep-learner api
@deeplearner_blueprint.route('/')
def testConnection():
  return umap.test()

# Hit this endpoint to compute umap features
# TODO this enpoint should take a bucket name as an argument
@deeplearner_blueprint.route('/features', methods = ['POST'])
def postFeatures(): 

  # BUCKET NAME THAT HAS WAV FILES
  bucketname = request.get_data(cache=True, as_text=True)

  # Remove the current files before downloading more files into the folder
  fs.remove_all_files_in_folder(downloadPath)

  # Downloads all the files from a bucket into a folder
  # Returns a list of the file path
  list_of_downloaded_file_paths = s3.downloadFiles(bucketname, foldername)

  mfcss_features = umap.computeFeatures(downloadPath)

  # TODO add into db
  
  return mfcss_features

@deeplearner_blueprint.route('/coordinates', methods = ['POST'])
def postSpectralSimilarityCoordinates(): 
  vector = df.getFeatures()
  # NOTE: FOR TESTING
  # vector = df.createTestVector()

  # print('testVector', vector)
  dataframe = umap.get_spec_sim_coordinates(vector)

  return dataframe