import os
import wget
import zipfile
import requests, zipfile
from io import BytesIO

# Download the zipped dataset
url = 'https://storage.googleapis.com/trainingdata-mlops/data.zip'
filename = url.split('/')[-1]
req = requests.get(url)
#webpage = urlopen(req).read()
zip_name = "data.zip"
wget.download(url, zip_name)

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()

os.remove(zip_name)
print('\nAll files are being extracted.')
