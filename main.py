from urllib.request import urlretrieve
from zipfile import ZipFile
import os
import requests
from bs4 import BeautifulSoup

VERSION_TXT = 'version.txt'
DST_PATH = './driver'
DRIVER_ZIP = f'{DST_PATH}/win.zip'
DRIVER_TMP = 'chromedriver-win64/chromedriver.exe'
DRIVER_EXE = f'{DST_PATH}/chromedriver.exe'
DRIVER_ABS_PATH_TXT = f'{DST_PATH}/path.txt'
CHROME_INDEX = 'https://googlechromelabs.github.io/chrome-for-testing'

# make driver dir
if not os.path.isdir(DST_PATH):
    print('create a folder.')
    os.mkdir(DST_PATH)

# get driver version
with open(VERSION_TXT, encoding='utf-16') as file:
    local_ver = file.read().strip().split('=')[-1]
    main_ver = local_ver.split('.')[0]
print('main ver: ', main_ver) # 87
print('ver: ', local_ver)     # 87.0.4280.141

# match ver in Chrome-Driver-Page
print('driver is updating...')
response = requests.get(CHROME_INDEX)
soup = BeautifulSoup(response.text, 'lxml')
ver = soup.find('code').string    # '87.0.4280.88'

# download driver zip
print('driver is updating..')
url = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{ver}/win64/chromedriver-win64.zip'
urlretrieve(url, DRIVER_ZIP)

# delete old driver.exe
print('driver is updating.')
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