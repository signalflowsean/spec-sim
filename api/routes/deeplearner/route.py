# ---- THIRD PARTY IMPORTS ----
import os, shutil

# pylint: disable=F0401
from flask import Blueprint, request, make_response, current_app as app
from werkzeug.utils import secure_filename

# ---- FIRST PARTY IMPORTS ----
# pylint: disable=E0611
from utils import umap, s3

# ---- CONSTANTS ----
ALLOWED_EXTENSIONS = {'wav', 'ds_store'}
BUCKET_NAME_PREFIX = 'audio-library'

# Register flask blueprint
deeplearner_blueprint = Blueprint('deeplearner', __name__)

# ---- ROUTES ----
# Hit this endpoint to test connection with the deep-learner api
@deeplearner_blueprint.route('/')
def testConnection():
  return umap.test()

# TODO this should go somewhere else
# Hit this endpoint to add audio library
# Req: directory containing mp3 files
# Res: name of s3-bucket that has uploaded files from Req
@deeplearner_blueprint.route('/audiolibrary', methods=['POST'])
def upload_audio_library_to_S3():  
  # grab files from the request objects
  files = request.files.getlist('file')

  # remove the files in the local file directory
  remove_all_files_in_folder(app.config['UPLOAD_FOLDER'])

  # check if the request object contains files
  if len(files) == 1 and files[0].filename == '':   
    return 'Error: no files have been found in the request'
    
  # save each file in folder to file system
  for file in files:
    filename = get_filename(file)
    # check that each file name has allowed extension
    if is_file_allowed(filename) == False: 
      return 'Error: File(s) do not have the correct extension'

    # save each file if it is not a folder
    if (is_folder(filename) == False):
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], get_filename(file)))

  # create s3 bucket 
  bucketname = s3.createBucket(BUCKET_NAME_PREFIX)

  # upload files to s3 bucket
  s3.uploadFiles(app.config['UPLOAD_FOLDER'], bucketname)
  
  # returns bucketname
  return bucketname

# Hit this endpoint to compute umap features
# TODO this enpoint should take a bucket name as an argument
@deeplearner_blueprint.route('/features', methods = ['POST'])
def postFeatures(): 

  # BUCKET NAME THAT HAS WAV FILES
  bucketname = request.get_data(cache=True, as_text=True)

  print('bucketname', bucketname)

  # ---- CONSTANTS ----
  foldername = 'downloaded_files_from_s3'
  downloadPath = './%s' % (foldername)

  # BUCKET NAME THAT HAS TXT FILES
  # bucketname = 'audio-libraryc605224e-226a-11ea-8f04-0242ac160002'

  # Remove the current files before downloading more files into the folder
  remove_all_files_in_folder(downloadPath)

  # Downloads all the files from a bucket into a folder
  # Returns a list of the file path
  list_of_downloaded_file_paths = s3.downloadFiles(bucketname, foldername)

  # NOTE THE ENCODING OF WAV BREAKS THE FILE READER -- only works for txt
  # printContentsOfFiles(list_of_downloaded_file_paths)

  return umap.computeFeatures(downloadPath)


# ---- UTILITIES ---- 
# TODO move these functions out into a util folder
# Prints contetnts of files
# Input: array of file paths that have been already downloaded from s3  
def printContentsOfFiles(file_paths): 
  for file_path in file_paths: 
    print('file contents:', open(file_path).read())    

def remove_all_files_in_folder(folder_path): 
  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
      if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
      elif os.path.isdir(file_path):
        shutil.rmtree(file_path)
    except Exception as e:
      print('Failed to delete %s. Reason: %s' % (file_path, e))

def is_folder(filename): 
  return get_file_ext(filename) == 'ds_store'

def get_file_ext(filename): 
  return '.' in filename and filename.rsplit('.', 1)[1].lower()

def get_filename(file): 
  return secure_filename(file.filename)

def is_file_allowed(filename):
  return get_file_ext(filename) in ALLOWED_EXTENSIONS   

