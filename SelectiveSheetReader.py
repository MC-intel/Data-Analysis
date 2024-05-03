#run this FIRST to get API key:

from google_drive_downloader import GoogleDriveDownloader as gdown
gdown.download_file_from_google_drive(file_id='1-IkKBuJXbac4XY4QTjy-x7Xuks5uaygs', dest_path='/content/something.data', unzip=False)






#run this SECOND to load into memory:

class structure_data:
  def __init__(self):
    
    while True:
      try:
        user_input = self.choose_data()
        new_data = self.main('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms', user_input['pt1'] , user_input['pt2'])
        break
      except Exception as E:
        print(E)
        print(" ")
        print("!!!!!!!!!!!!!!!!!!!!!")
        print("ERROR Try new input.")
        print("Inputs MUST resemble examples!")
        print(" ")

    import pandas as pd
    data_frame = pd.DataFrame(new_data)
    self.data_frame = data_frame
    
  def main(self, sheetID, pt1, pt2):
    #service = get_sheets_key()  #authentication process
    import pickle
    with open('something.data', 'rb') as ree:
      service = pickle.load(ree)
    
    # Call the Sheets API
    sheet = service.spreadsheets()
    #THIS IS FROM EXAMPLE SHEET 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
    SAMPLE_RANGE_NAME = 'Class Data!' + pt1 + ':' + pt2
    result = sheet.values().get(spreadsheetId=sheetID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    

    return values

  def choose_data(self):
    #pairs with module
    print("CHOOSE SECTION:")
    print("ROWS A-F   COLLUMNS: 1-32")
    print("EXAMPLE: A1 to F32")
    print(" ")
    print("Start of Section:  ")
    print("EX. A1")
    print(" ")
    pt1 = input()
    print("End of Section: ")
    print("EX. F32")
    print(" ")
    pt2 = input()

    container = {}
    container['pt1'] = pt1
    container['pt2'] = pt2
    return container

  def organize(self):
    data_frame = self.data_frame
    import pandas as pd
    print("CSV FileName: ")
    file_name = input()
    headers = data_frame.iloc[0]
    new_df  = pd.DataFrame(data_frame.values[1:], columns=headers)
    new_df.to_csv(file_name + '.csv')
    print(" ")
    print("DONE! Your selected data has been compiled in the .csv file you created!")
    print(" ")
    print("Here is an example of what it should look like:")
    print(" ")
    return new_df
    
    
    
    
    
    
    
    #run this LAST to run my program:

def main():
  mychart = structure_data()
  finalorganize = mychart.organize()
  print(finalorganize)
  
if __name__ == '__main__':
  main()
