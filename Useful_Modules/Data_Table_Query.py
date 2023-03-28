#query specfic data from tables

def query_dataframes(filepath, column, value):
  import pandas as pd
  data = pd.read_csv(str(filepath))
  table = pd.DataFrame(data)
  pd.DataFrame.to_html()

  sort_values = df_dict = table.to_dict(orient='list')
  filter = df_sorted_matching = table.sort_values(by=str(column)).loc[table[str(column)] == str(value)]

  print(list(table))
  print(filter.head(3))

  Q = data.query(f"{column} == {value}")
  return Q



#professional example

def check_calibration(report_file, date)
  import pandas as pd

  csv = pd.read_csv(str(report_file))
  df = pd.DataFrame(csv)
  df = df.drop(df.columns[[0]], axis=1)

  df.rename(columns={'Next Calibration Date': 'Calibration'}, inplace=True)
  df.rename(columns={'Parent Location': 'Location'}, inplace=True)
  df.rename(columns={'Asset ID': 'ID'}, inplace=True)
  df.rename(columns={'Asset Name': 'Name'}, inplace=True)
  df.rename(columns={'Next Vendor PM date': 'PM'}, inplace=True)

  df

  df = df.query(f"Calibration == {date}")
  df

  csv = pd.DataFrame.to_csv(df)
  with open('filtered_report.csv', 'w') as f:
    f.write(csv)