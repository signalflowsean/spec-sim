CREATE TABLE IF NOT EXISTS spectralSimilarity ( 
  ID int NOT NULL, 
  fileName VARCHAR(255) NOT NULL, 
  relativePath VARCHAR(255) NOT NULL, 
  mfcc_raw_vector VARCHAR(255)
  mfcc_std_dev_vector VARCHAR(255)
  mfcc_mean_vector VARCHAR(255)
  mfcc_avg_diff_vector VARCHAR(255)
  mfcc_fixed_vector VARCHAR(255)
  x_corr VARCHAR(255)
  y_corr VARCHAR(255)
  cluster VARCHAR(255)
  PRIMARY KEY (ID)
)