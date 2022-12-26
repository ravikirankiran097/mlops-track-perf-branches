import os
import wget
import zipfile
import requests, zipfile
from io import BytesIO

# Download the zipped dataset
from urllib.request import Request, urlopen

req = Request(
    url='https://storage.googleapis.com/trainingdata-mlops/data.zip', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()


#url = 'https://storage.googleapis.com/trainingdata-mlops/data.zip'
#filename = url.split('/')[-1]
#req = requests.get(url)
#webpage = urlopen(req).read()
#zip_name = "data.zip"
#wget.download(url, zip_name)

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()

os.remove(zip_name)
print('\nAll files are being extracted.')
