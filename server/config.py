import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object): 
  # S3 CONFIG
  UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or './uploaded_files_to_s3'

  # DB CONFIG
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
  
  SQLALCHEMY_TRACK_MODIFICATIONS = False
