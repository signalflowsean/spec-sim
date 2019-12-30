# ---- THIRD PARTY IMPORTS ---- 
# pylint: disable=F0401
import os, librosa, librosa.display
import numpy as np, pandas as pd

# ---- FIRST PARTY IMPORTS ---
# pylint: disable=F0401
from .. import df

# ---- CONTANTS ----
sample_rate = 44100
mfcc_size = 13
file_extentsion = '.wav'

def computeFeatures(downloadPath): 
  length_of_downloaded_files = len(os.listdir(downloadPath))

  # Initializes dataframe to store the data!
  df.initializeDataFrame(length_of_downloaded_files)
  
  # Initialize mfccs features data structure 
  mfccs_features = np.zeros((length_of_downloaded_files, 39))

  # LOOP THROUGH WAV FILES
  for i in range(0, length_of_downloaded_files):
    # FIND THE FILE NAME AND FILE PATH OF SOUND FILES
    file = os.listdir(downloadPath)[i] 
    df.addItemAtIndex('file_name', i, file)

    file_path = os.path.join(downloadPath, file)
    df.addItemAtIndex('file_path', i, file_path)

    # Load the audio
    pcm_data, _ = librosa.load(file_path)

    # MFCC VECTOR
    # Compute a vector of 13 * n mfccs
    feature_sequence = librosa.feature.mfcc(pcm_data, sample_rate, n_mfcc=mfcc_size)    
    # Take the transpose to get n * 13
    feature_sequence = feature_sequence.transpose()
    df.addItemAtIndex('mfcc_raw_vector', i, np.array2string(feature_sequence))
    
    # STANDARDIZED THE MFCC OUTPUT TO BE A VECTOR OF A FIXED OUTPUT BY: 
    # 1. Get the standard deviation
    stddev_features = np.std(feature_sequence, axis=0)
    df.addItemAtIndex('mfcc_std_dev_vector', i,  np.array2string(stddev_features))
    
    # 2.Get the mean
    mean_features = np.mean(feature_sequence, axis=0)
    df.addItemAtIndex('mfcc_mean_vector', i,  np.array2string(mean_features))

    # 3. Get the average difference of the features
    average_difference_features = np.zeros((13,))
    for j in range(0, len(feature_sequence)-1, 2):
      average_difference_features += feature_sequence[j] - feature_sequence[j+1]

    average_difference_features /= (len(feature_sequence) // 2)   
    average_difference_features = np.array(average_difference_features)
    df.addItemAtIndex('mfcc_avg_diff_vector', i,  np.array2string(average_difference_features))
    
    # Concatenate the features to a single feature vector
    concat_features_features = np.hstack((stddev_features, mean_features))
    concat_features_features = np.hstack((concat_features_features, average_difference_features))
    df.addItemAtIndex('mfcc_fixed_vector', i,  np.array2string(concat_features_features))    
    
    # Add the single feature vector to an array of aggregated
    mfccs_features[i] = concat_features_features
    df.printDataFrame(); 
  
  return np.array_str(mfccs_features)
