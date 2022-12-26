from zipfile import ZipFile
from urllib.request import urlopen   
import pandas as pd
import os

URL = 'https://storage.googleapis.com/trainingdata-mlops/data.zip'

# open and save the zip file onto computer
url = urlopen(URL)
output = open('data.zip', 'wb')    # note the flag:  "wb"        
output.write(url.read())
output.close()

# read the zip file as a pandas dataframe
df = pd.read_csv('data.zip')    #zip files       

# if keeping on disk the zip file is not wanted, then:
os.remove(zipName)   # remove the copy of the zipfile on disk
print('\nAll files are being extracted.')
