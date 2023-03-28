#serialized data to csv

def pickle_tocsv(filepath):
  import pickle 
  import pandas as pd

  pik = pd.read_pickle(str(filepath))
  df = pd.DataFrame(pik)
  csv = pd.DataFrame.to_csv(df)
  with open('filename.csv', 'w') as f:
    f.write(csv)

  return df

