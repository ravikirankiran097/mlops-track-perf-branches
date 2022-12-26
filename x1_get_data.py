import os
import wget
import zipfile
import urllib.request

# Download the zipped dataset
req = urllib.request.Request(url="https://storage.googleapis.com/trainingdata-mlops/data.zip",
headers={'User-Agent': 'Mozilla/5.0'}
handler = urllib.request.urlopen(req)
#url = 'https://storage.googleapis.com/trainingdata-mlops/data.zip'
#webpage = urlopen(req).read()

zip_name = "data.zip"
wget.download(url, zip_name)

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()

os.remove(zip_name)
print('\nAll files are being extracted.')
