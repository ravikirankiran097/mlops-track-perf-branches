import os
import wget
import zipfile
from urllib import request
from urllib.request import Request, urlopen

# Download the zipped dataset
url = "https://storage.googleapis.com/trainingdata-mlops/data.zip"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()
print(webpage[:500])

#url = 'https://storage.googleapis.com/trainingdata-mlops/data.zip'
#webpage = urlopen(req).read()

zip_name = "data.zip"
wget.download(url, zip_name)

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()

os.remove(zip_name)
print('\nAll files are being extracted.')
