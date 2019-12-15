# ---- THIRD PARTY IMPORTS ---- 
# pylint: disable=F0401
from flask import Flask
from flask import request

# ---- FIRST PARTY IMPORTS ----
import umap

# ---- INITIALIZE FLASK APP ----
app = Flask(__name__)

# ---- ROUTES ----
# Hit this endpoint to test connection with the deep-learner api
@app.route('/')
def testConnection():
  return umap.test()

# Hit this endpoint to compute umap features
@app.route('/features', methods = ['POST', 'GET'])
def postFeatures(): 
  if request.method == 'GET':
    return umap.computeFeatures()

if __name__ == "__main__":
  app.run()