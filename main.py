from urllib.request import urlretrieve
from zipfile import ZipFile
import os
import requests
import subprocess

DST_PATH = './driver'
DRIVER_ZIP = f'{DST_PATH}/win.zip'
DRIVER_TMP = 'chromedriver-win64/chromedriver.exe'
DRIVER_EXE = f'{DST_PATH}/chromedriver.exe'
CHROME_QUERY = 'https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_'
CHROMEDRIVER_URL = 'https://storage.googleapis.com/chrome-for-testing-public/{}/win64/chromedriver-win64.zip'

# make driver dir
if not os.path.isdir(DST_PATH):
    print('create a folder.')
    os.mkdir(DST_PATH)

# get chrome version
local_ver = subprocess.check_output('reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version').decode('utf-8', 'ignore').strip().split()[-1]
main_ver = local_ver.split('.')[0]

# get version of Chrome-Driver
ver = requests.get(CHROME_QUERY + main_ver).text    # '87.0.4280.88'
print('chrome ver: ', main_ver) # 87
print('driver ver: ', ver)     # 87.0.4280.141

# download driver zip
url = CHROMEDRIVER_URL.format(ver)
urlretrieve(url, DRIVER_ZIP)

# delete old driver.exe
if os.path.isfile(DRIVER_EXE):
    os.remove(DRIVER_EXE)

# unzip
with ZipFile(DRIVER_ZIP, 'r') as zf:
    zf.extract(DRIVER_TMP, path=DST_PATH)

# move chromedriver.exe to upper dir
os.rename(f'{DST_PATH}/{DRIVER_TMP}', DRIVER_EXE)

# remove zip
os.remove(DRIVER_ZIP)
os.rmdir(f'{DST_PATH}/chromedriver-win64/')
print('DONE!')