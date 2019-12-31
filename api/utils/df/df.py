# ---- THIRD PARTY IMPORTS ----
# pylint: disable=F0401
import os, librosa, librosa.display
import numpy as np, pandas as pd

# ---- CONTANTS ----
# Shape for test vector
shape = [13, 39]

# GLOBAL REFERENCE OF SPECTRAL SIMILARITY DATAFRAME
spectral_similarity_df = pd.DataFrame();

features = np.zeros((13, 39))

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
def saveFeatures(_features): 
  features = _features

def getFeatures():
  return features

def getDataFrameAsString(): 
  return spectral_similarity_df.to_string()

def printDataFrame():
  print('dataFrame', spectral_similarity_df.to_string())

# def concatenateFeatures(): 

# NOTE: for testing purpposes
def createTestVector():
  return np.random.rand(shape[0], shape[1])

def stringToVec(string): 
  return np.fromstring(string, '13, 19')

# def printShape():

def get_fake_features_as_string(): 
  return '[[ 1.62872635e+02  2.60282574e+01  4.60925674e+01  8.25003624e+00 1.76867046e+01  5.93648624e+00  9.36491680e+00  4.70647526e+00 8.48815632e+00  4.75637293e+00  5.53784132e+00  3.87593937e+00 4.29679966e+00 -4.62556335e+02  1.20702332e+02  3.80869789e+01 3.71333199e+01  1.12016993e+01  9.14768124e+00  5.35314226e+00 7.27356720e+00  2.28162289e+00 -7.30580151e-01 -1.93674433e+00 1.88629127e+00  3.36476660e+00  1.24451644e+01  9.66705746e-01 -2.19829209e+00 -7.07901566e-01 -1.35992923e+00 -3.89582418e-01 -2.99124568e-01  3.76277032e-01  2.58199581e-01 -1.98701448e-01 -5.55212908e-01 -3.22666296e-01 -1.60612016e-01] [ 9.13304291e+01  4.78269691e+01  1.21876621e+01  1.11506567e+01 1.27210846e+01  4.17801237e+00  4.18983126e+00  4.69804001e+00 5.58554602e+00  6.82677460e+00  7.05270290e+00  6.33868122e+00 5.23120165e+00 -5.41328796e+02  1.40614059e+02  5.24759979e+01 4.12958221e+01  1.18131380e+01  1.62199268e+01  5.55602026e+00 1.09834881e+01 -1.53761423e+00  8.57277870e+00 -3.20309520e+00 6.17302084e+00 -1.52738619e+00  8.51823215e+00 -2.47961087e+00 -8.83295520e-01  2.71000829e-01 -2.83308079e-01  6.83859167e-01 1.09508802e-01  7.85493933e-02 -2.48324606e-01  6.90002211e-01 -1.20948843e-01  9.07813927e-01 -4.97670996e-02] [ 8.47439117e+01  4.36747322e+01  8.10285759e+00  1.07190313e+01 1.07974377e+01  4.65229273e+00  4.79011154e+00  5.12192297e+00 3.82588506e+00  6.78439379e+00  9.28331089e+00  7.75946236e+00 3.72165489e+00 -5.42797180e+02  1.37315140e+02  5.77486839e+01 4.15584373e+01  1.28626328e+01  1.62628956e+01  7.93053532e+00 8.96515560e+00  2.18538737e+00  1.02441416e+01 -3.57996321e+00 8.34768200e+00 -8.21632087e-01  7.10928726e+00 -1.65529142e+00 7.17305865e-01 -5.01168387e-01 -8.52463893e-01  5.19595197e-01 -1.80957266e-01 -8.65840380e-02 -4.39269656e-01 -5.01853934e-01 -8.28855847e-02  6.05292625e-01 -5.80008839e-02] [ 1.44372025e+02  1.77658386e+01  3.85479393e+01  6.53326082e+00 1.25205812e+01  5.11250782e+00  6.82888174e+00  4.56291533e+00 5.54333878e+00  3.05151057e+00  5.09567595e+00  4.40664911e+00 7.01168442e+00 -4.51732758e+02  9.81541061e+01  4.68094902e+01 4.05696068e+01  1.66671047e+01  1.24783726e+01  8.26248932e+00 8.60442066e+00  3.90994525e+00  4.93974257e+00  2.39854240e+00 7.28323102e-01 -1.70020878e+00  9.87685102e+00  7.16980375e-01 -2.05167647e+00 -5.39767298e-01 -6.31805420e-01 -1.73544193e-01 -1.33667329e-01  2.15528052e-01  8.23460201e-02  3.22860257e-01 1.60677612e-01 -5.24315706e-02 -5.70364860e-01] [ 9.80847397e+01  3.83788605e+01  1.93250809e+01  5.77058697e+00 7.82779026e+00  5.25626802e+00  5.17824650e+00  4.14105558e+00 3.96270275e+00  3.76884103e+00  2.87768340e+00  3.80112314e+00 5.58894444e+00 -4.54521973e+02  9.85160294e+01  5.48653183e+01 3.79800301e+01  2.32490463e+01  1.38169994e+01  7.70034218e+00 7.17275381e+00  5.54001188e+00  3.07422042e+00  2.93593287e+00 2.56852698e+00  1.47221863e+00  8.02188756e+00  3.05887413e+0 -1.12240571e+00 -4.18920224e-01 -5.03998793e-01 -4.68855968e-01 -5.82686287e-01 -1.69993740e-01  3.63976951e-01  7.50936490e-01 9.57660909e-01 -4.07929443e-02 -5.87934040e-01] [ 9.26980896e+01  2.31053791e+01  2.74790249e+01  7.57764292e+00 1.46932716e+01  5.47281361e+00  6.54764509e+00  1.00472689e+01 1.09051380e+01  7.55392742e+00  6.66787863e+00  6.47158575e+00 1.17070522e+01 -5.20994019e+02  1.33640121e+02  5.88983269e+01 3.45529251e+01  1.31362019e+01  1.00576935e+01  6.91044521e+00 1.15949936e+01  8.78956604e+00  4.82038784e+00  2.96818805e+00 -5.46970725e-01 -3.26958799e+00  8.84071296e+00 -7.47787476e-01 -1.11484947e+00  4.69855990e-01 -9.97837986e-01 -7.24218530e-01 -1.20317105e+00 -4.09815993e-03  6.44587291e-01  2.91269434e-01 3.41106515e-01  6.43326622e-01 -6.61539872e-01] [ 5.19242439e+01  3.11337872e+01  1.18233318e+01  7.70911217e+00 4.51453114e+00  5.66318798e+00  5.83911991e+00  4.37251329e+00 3.82267690e+00  3.63147783e+00  3.83797765e+00  3.36424470e+00 3.38888669e+00 -4.59721252e+02  1.07704567e+02  6.93353653e+01 4.12193184e+01  2.44758148e+01  1.65923367e+01  1.14535809e+01 9.25151730e+00  7.33218718e+00  5.68653059e+00  4.53396606e+00 4.20845413e+00  3.89428759e+00  2.42437904e+00  1.67337691e+00 6.36368851e-01 -1.55219932e-01 -2.41379496e-01 -2.06424734e-01 -3.62825081e-01 -2.09165865e-01 -7.62414932e-03 -2.60196515e-05 -2.96364613e-03  6.89709534e-02  2.19359006e-02] [ 7.98536072e+01  4.02285767e+01  1.05647697e+01  4.48430061e+00 5.25596714e+00  4.22135305e+00  6.74541473e+00  6.15889740e+00 7.33886623e+00  6.56968403e+00  1.01990108e+01  7.94603109e+00 4.44112062e+00 -5.47535156e+02  1.43212234e+02  6.27454987e+01 3.73824005e+01  1.63068466e+01  1.38781147e+01  9.26846886e+00 8.79682636e+00  2.00689411e+00  9.69921589e+00 -5.61236954e+00 7.54692125e+00 -2.79549122e+00  8.71908061e+00 -2.80664437e+00 -9.43329211e-01 -2.42563248e-01 -5.60528155e-01 -1.71280119e-01 -1.35311370e-01 -6.71275065e-01 -5.76963831e-01  8.07867801e-01 -1.04586241e-01  9.67750143e-01 -3.85147580e-01] [ 6.72767563e+01  3.15050049e+01  1.26238413e+01  9.51377392e+00 4.11943150e+00  4.38451147e+00  4.08392525e+00  3.53198481e+00 4.28387403e+00  3.59261847e+00  3.66671205e+00  2.67464471e+00 2.96447945e+00 -4.72238129e+02  9.54749985e+01  6.38305511e+01 4.04521217e+01  2.22636719e+01  1.28917942e+01  7.49812365e+00 6.34568167e+00  5.03663492e+00  3.71085596e+00  2.37221193e+00 2.13409686e+00  2.07970285e+00  4.95483246e+00  2.50233073e+00 8.68064880e-02 -8.15464973e-02  2.07061332e-01 -6.35581017e-0 -2.79816941e-01  5.52968400e-02  2.10382767e-01  5.34037709e-01 6.19161499e-01  3.59944577e-01  1.69623555e-01] [ 5.62603607e+01  3.93217659e+01  1.32370968e+01  5.38912153e+00 3.74104619e+00  4.50790834e+00  4.75793219e+00  5.48619843e+00 4.20074415e+00  2.75646973e+00  2.81612825e+00  3.43916464e+00 3.17782521e+00 -4.84582703e+02  1.05746269e+02  6.90862579e+01 4.15523109e+01  2.22370625e+01  1.27219028e+01  9.72727489e+00 8.19664288e+00  6.55532074e+00  4.68692398e+00  3.09789038e+00 1.59103847e+00  1.27452803e+00  5.29181773e+00  3.56758041e+0 -3.71812948e-01 -5.61488469e-01 -6.66552925e-01 -4.67152898e-0-6.43723575e-01 -3.15170463e-01 -8.78339609e-03 -1.51588599e-02 3.64275307e-01 -3.68107001e-02 -1.96546878e-01] [ 8.00210800e+01  4.70373688e+01  1.86375904e+01  1.13390799e+01 1.05810843e+01  9.18992901e+00  4.45310593e+00  4.34528494e+00 4.60742569e+00  4.88499117e+00  5.53862762e+00  4.02944613e+00 4.18213224e+00 -5.43073792e+02  1.39975693e+02  5.42067528e+01 4.34502640e+01  1.25775023e+01  1.90506268e+01  4.87854767e+00 1.11106663e+01  3.92760086e+00  4.66182756e+00  1.18437815e+00 2.84034729e+00 -4.65203114e-02  7.81302795e+00 -3.71716843e+00 -8.63301214e-01  1.58571593e+00 -3.03632959e-01  7.93927145e-01 3.61981094e-02 -2.42515683e-01 -1.81868362e-01 -1.30366735e-01 -2.24496921e-01 -2.87092280e-01  2.31394795e-01] [ 1.42031372e+02  9.47982330e+01  1.80213490e+01  2.68969364e+01 2.12947426e+01  1.53443289e+01  1.01971836e+01  6.90993357e+00 7.31873655e+00  5.10829210e+00  6.44623041e+00  4.02283812e+00 3.33464503e+00 -4.35832977e+02  5.45394173e+01  5.37721024e+01 6.27975769e+01 -4.45444822e+00  3.15344543e+01 -2.63312197e+00 1.74570637e+01 -3.57704544e+00  2.95634055e+00  6.07605743e+00 5.92777133e-01 -1.33518302e+00  8.54435036e+00 -1.52187293e+00 -1.03626066e+00  2.84064611e-01 -1.25742722e+00 -1.76755847e-01 -7.74313461e-01  5.22520470e-02 -7.54862034e-01 -7.47598983e-01 -7.68816973e-01  9.72806143e-03  9.43108680e-02] [ 8.18887329e+01  4.50927277e+01  1.24711809e+01  1.06449089e+01 1.02927523e+01  8.54291058e+00  4.85130119e+00  5.56493187e+00 3.25683904e+00  4.16170025e+00  4.94620180e+00  5.03120089e+00 4.15073252e+00 -5.48781189e+02  1.42195801e+02  5.46601639e+01 4.10798950e+01  1.13170576e+01  1.91280270e+01  4.10404825e+00 1.08410692e+01 -1.17488936e-01  3.76261783e+00  9.82034028e-01 1.99059701e+00  3.32722962e-01  9.33304537e+00 -3.74386813e+00 -6.04998075e-01  1.04844944e+00 -2.33242200e-01  9.26681665e-03 -2.51110049e-01  3.13758905e-01 -4.70254518e-01 -6.53012344e-01 -5.09969184e-01 -6.03640822e-01 -5.48714154e-01]]'

