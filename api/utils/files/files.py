# --- THIRD PARTY IMPORTS ----
import os, shutil
from werkzeug.utils import secure_filename

# ---- CONSTANTS ----
ALLOWED_EXTENSIONS = {'wav', 'ds_store'}

# Prints contents of files
# Input: array of file paths that have been already downloaded from s3  
def printContentsOfFiles(file_paths): 
  for file_path in file_paths: 
    print('file contents:', open(file_path).read())    

# Removes all the files in a folder
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

# Checks if it is a valid folder
def is_folder(filename): 
  return get_file_ext(filename) == 'ds_store'

def get_file_ext(filename): 
  return '.' in filename and filename.rsplit('.', 1)[1].lower()

def get_filename(file): 
  return secure_filename(file.filename)

def is_file_allowed(filename):
  return get_file_ext(filename) in ALLOWED_EXTENSIONS 

