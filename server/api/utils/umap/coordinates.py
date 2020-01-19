# ---- THIRD PART IMPORTS ----
# pylint: disable=F0401
import os, librosa, librosa.display
import numpy as np, pandas as pd
import umap

# ____ FIRST PARTY IMPORTS ----
# from .. import df

# SORT FEATURES BY SPECTRAL SIMILARITY
# UMAP
from sklearn.preprocessing import MinMaxScaler

def _get_scaled_umap_embeddings(features, neighbour, distance):
  # contstruct a UMAP object
  embedding = umap.UMAP(n_neighbors=neighbour, min_dist=distance, metric='correlation').fit_transform(features)
  
  scaler = MinMaxScaler()
  scaler.fit(embedding)
  return scaler.transform(embedding)

def get_spec_sim_coordinates(mfccs_features):
  # EXAMPLES OF UMAP PARAMATERS
  # The lower the parameters - the the more local structure there is!
  # neighbours = [5, 10, 15, 30, 50]
  # distances = [0.000, 0.001, 0.01, 0.1, 0.5]
  neighbour = 30
  distance = 0.001

  umap_mfccs = _get_scaled_umap_embeddings(mfccs_features, neighbour, distance)

  # Finds x and y coordinates
  for i in range (0, len(umap_mfccs)): 
    point = umap_mfccs[i]
    # df.addItemAtIndex('x_corr', i, point[0])
    # df.addItemAtIndex('y_corr', i, point[1])

  # df.printDataFrame()
  # return df.getDataFrameAsString()
  return 'cheese'
