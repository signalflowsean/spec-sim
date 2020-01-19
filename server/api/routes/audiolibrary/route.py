
# ---- THIRD PARTY IMPORTS ----- 
import os
# pylint: disable=F0401
from flask import Blueprint, request, current_app as app

# ---- FIRST PARTY IMPORTS ---- 
# pylint: disable=E0611
from utils import s3, files as fs

# ---- CONSTANTS ----
BUCKET_NAME_PREFIX = 'audio-library'

# Register flask blueprint
audiolibrary_blueprint = Blueprint('audiolibrary', __name__)

# Hit this endpoint to add audio library
# Req: directory containing mp3 files
# Res: name of s3-bucket that has uploaded files from Req
@audiolibrary_blueprint.route('/audiolibrary', methods=['POST'])
def upload_audio_library_to_S3():  
  # grab files from the request objects
  files = request.files.getlist('file')

  # remove the files in the local file directory
  fs.remove_all_files_in_folder(app.config['UPLOAD_FOLDER'])

  # check if the request object contains files
  if len(files) == 1 and files[0].filename == '':   
    return 'Error: no files have been found in the request'
    
  # save each file in folder to file system
  for file in files:
    filename = fs.get_filename(file)
    # check that each file name has allowed extension
    if fs.is_file_allowed(filename) == False: 
      return 'Error: File(s) do not have the correct extension'

    # save each file if it is not a folder
    if (fs.is_folder(filename) == False):
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], fs.get_filename(file)))

  # create s3 bucket 
  bucketname = s3.createBucket(BUCKET_NAME_PREFIX)

  # upload files to s3 bucket
  s3.uploadFiles(app.config['UPLOAD_FOLDER'], bucketname)
  
  # returns bucketname
  return bucketname
