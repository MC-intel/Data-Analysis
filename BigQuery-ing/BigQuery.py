# HANDLE BIG QUERY DATA

!gcloud auth application-default login  # Get key
!gcloud config set project PROJECT-NAME  # Assign key


# Ping Data Warehouse and get SQL data
def sql_pull(script) -> str:
  import pandas as pd
  import pandas_gbq as pg
  from google.cloud import bigquery

  # Get Big Query
  project = 'PROJECT-NAME'
  client = bigquery.Client(project=project)

  try:
    # Preform a query
    SQL = script
    query_job = client.query(SQL) # API request
    rows = query_job.result()

    if query_job.state == 'DONE': # DataFrame
      dframe = query_job.to_dataframe()
      dframe.to_csv('data.csv', index=False) # Prepare .csv
      return dframe
    else:
      print(query_job.result())

  except:
    print('Bad input')