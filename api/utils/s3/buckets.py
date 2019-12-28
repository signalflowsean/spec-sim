# ---- Third party imports ----
import os
# pylint: disable=F0401
import boto3 # - manipulating s3 buckets 
from uuid import uuid1 # - creating unique ids

# ---- First party imports ----
# pylint: disable=E0611
# from config import S3_KEY, S3_SECRET

S3_KEY = os.environ.get('S3_KEY')
S3_SECRET = os.environ.get('S3_SECRET')

# Create reference to s3
def _getS3Ref(): 
  return boto3.client('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)

# Reference of s3 that gets passed around
s3 = _getS3Ref()

# ---- GET METADATA ----
# Retrieve all of the files in a bucket - as a obj-list
def _getAllFilesInABucket(bucket_name): 
  # TODO validate if there are contents of the bucket
  return s3.list_objects_v2(Bucket=bucket_name)['Contents']

# Retrieve all of the file names in a bucket - as a list
def getAllFilesNamesInABucket(bucket_name): 
  return list(map(lambda x: x['Key'], _getAllFilesInABucket(bucket_name)))

# Retrieve all of the file names - as an obj-list
def _getAllFilesNamesInABucketAsAnObjList(bucket_name): 
  return [{'Key': obj} for obj in getAllFilesNamesInABucket(bucket_name)]

# ---- CREATE BUCKET AND UPLOAD FILES --- 
# Creates a bucket
def createBucket(prefix): 
  bucket_name = _createBucketName(prefix)
  print('Creating bucket : %s' % (bucket_name))
  s3.create_bucket(Bucket=bucket_name)
  return bucket_name

# Create bucket name - must be unique per region
def _createBucketName(prefix): 
  return ''.join([prefix, str(uuid1())])

# Uploads the given file using a managed uploader, which will split up large files automatically and upload parts in parallel.
def _uploadFile(file_name, bucket_name, file): 
  s3.upload_file(file_name, bucket_name, file)

# Loops through the files in the directory and uploads them to a bucket
def uploadFiles(folder_path, bucket_name): 
  print('Uploading files from folder: %s into bucket: %s' % (folder_path, bucket_name))
  for root, dirs, files in os.walk(folder_path):
    for file in files: 
      _uploadFile(os.path.join(root, file), bucket_name, file)

# ---- DELETE BUCKET AND REMOVE FILES ----
# Deletes all of the files in a bucket
def _deleteAllFilesInBucket(bucket_name): 
  s3.delete_objects(
    Bucket=bucket_name, 
    Delete={'Objects': _getAllFilesNamesInABucketAsAnObjList(bucket_name)})

# Deletes a bucket
def deleteBucket(bucket_name): 
  print('Deleting bucket: %s' % bucket_name)
  # In order to delete a bucket all of the files must be removed
  _deleteAllFilesInBucket(bucket_name)
  s3.delete_bucket(Bucket=bucket_name)

# ----  DOWNLOADING FILES(s) ----
# Downloads a single file from a bucket
# Returns download path of downloaded file
def _downloadFile(bucket_name, file_name, folder_name): 
  download_path = '%s/%s' % (folder_name, file_name)
  s3.download_file(bucket_name, file_name, download_path)
  return download_path

# Downloads all of the files from a bucket
def downloadFiles(bucket_name, folder_name):
  print('Downloading files from bucket: %s' % (bucket_name))

  # TODO check if the directory is empty -- if it is make the directory
  # initialize an array for the files names to be stored in
  files = []
  for file_name in getAllFilesNamesInABucket(bucket_name):
    files.append(_downloadFile(bucket_name, file_name, folder_name))
