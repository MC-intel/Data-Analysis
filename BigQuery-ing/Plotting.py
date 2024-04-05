 #Visualization
def visual(csv_path) -> str:
  import rpy2 as R
  import rpy2.robjects

  import rpy2.robjects.packages as rpackages
  from rpy2.robjects.packages import importr

  import rpy2.robjects.lib.ggplot2 as gp
  from rpy2.robjects import rl

  utils = importr('utils')
  dfile = utils.read_csv(csv_path)

  # Create graph
  graph = (gp.ggplot(dfile) +
      gp.aes(x=rl('temperature'),
              y=rl('sensorName'),
              color=rl('humidity'),
              size=rl('temperature')) +
      gp.geom_point() +
      gp.scale_color_continuous(trans='log10'))

  # Produce image
  from rpy2.ipython.ggplot import image_png
  vis = image_png(graph)
  return vis

  with open('image.raw', 'w') as wi:
    wi.write(vis)
    
    visual('/content/test.csv')
    

#error handling
import pandas as pd
import pandas_gbq as pg
from google.cloud import bigquery

def sql_pull(project: str, script: str) -> pd.DataFrame:
    """Execute a SQL query and return the results as a Pandas DataFrame.
    
    Args:
        project (str): The GCP project to use.
        script (str): The SQL script to execute.
        
    Returns:
        pd.DataFrame: A Pandas DataFrame containing the query results.
        
    Raises:
        Exception: If an error occurs while executing the query.
    """
    client = bigquery.Client(project=project)
    
    try:
        query_job = client.query(script)
        rows = query_job.result()
        
        if query_job.state == 'DONE':
            dframe = query_job.to_dataframe()
            dframe.to_csv('data.csv', index=False)
            return dframe
        else:
            raise Exception(query_job.result())
    except Exception as e:
        print(f'Error executing query: {e}')