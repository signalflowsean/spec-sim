
# pylint: disable=F0401
import os, librosa, librosa.display
import numpy as np, pandas as pd

# GLOBAL REFERENCE OF SPECTRAL SIMILARITY DATAFRAME
spectral_similarity_df = pd.DataFrame();

# This is called when the /features endpoint is hit
def initializeDataFrame(length_of_downloaded_files): 
  # Initializing data frame
  data = np.zeros((length_of_downloaded_files, 10))

  spectral_similarity_df =  pd.DataFrame( data, 
    columns=[ 'file_name', 'relative_path', 'mfcc_raw_vector', 'mfcc_std_dev_vector', 'mfcc_mean_vector', 
              'mfcc_avg_diff_vector', 'mfcc_fixed_vector', 'x_corr', 'y_corr', 'cluster'])

# Add an item given the column name and row number 
def addItemAtIndex(column_name, index_row, value): 
  spectral_similarity_df.loc[index_row, column_name] = value

# TODO be bale to dd more than one item to the df at a time

def printDataFrame():
  print('dataFrame', spectral_similarity_df.to_string())