def hood_chart():
  import pandas as pd
  import seaborn as sb

  Y_axis = ['Y1','Y2', 'Y3']
  sheet_title = {'Index': Y_axis,
                'X1': [0,0,0],
                'X2': [0,0,0],
                'X3': [0,0,0]}
  sheet = pd.DataFrame(sheet_title)
  sheet.set_index('Index', inplace=True)
  
  data_file = sheet.to_csv('particle_read')
  H = sb.heatmap(sheet, vmin=0, vmax=1, linewidths=.05, cmap= 'YlGnBu')

  print('HeatMap')
  return(sheet)
  print(' ')
  return(H)

hood_chart()
