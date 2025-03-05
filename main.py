from urllib.request import urlretrieve
from zipfile import ZipFile
import os
import re
import requests
from bs4 import BeautifulSoup

VERSION_TXT = 'version.txt'
DST_PATH = './driver'
DRIVER_ZIP = f'{DST_PATH}/win.zip'
DRIVER_EXE = f'{DST_PATH}/chromedriver.exe'
DRIVER_LICENSE = f'{DST_PATH}/LICENSE.chromedriver'
DRIVER_ABS_PATH_TXT = f'{DST_PATH}/path.txt'
CHROME_INDEX = 'https://chromedriver.chromium.org/downloads'

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
tmp = soup.find('a', {'href': re.compile(main_ver)}).string    # 'ChromeDriver 87.0.4280.88'

# download driver zip
print('driver is updating..')
ver = tmp.split(' ')[-1]
url = f'https://chromedriver.storage.googleapis.com/{ver}/chromedriver_win32.zip'
urlretrieve(url, DRIVER_ZIP)

# delete old driver.exe
print('driver is updating.')
if os.path.isfile(DRIVER_EXE):
    os.remove(DRIVER_EXE)

# unzip
with ZipFile(DRIVER_ZIP, 'r') as zf:
    zf.extractall(path=DST_PATH)

# create txt file that has driver absolute path
# DRIVER_ABS_PATH = os.path.abspath(DRIVER_EXE)
# with open(DRIVER_ABS_PATH_TXT, 'w') as file:
#     file.write(DRIVER_ABS_PATH)
#     print('create txt file that has driver absolute path.')

# remove zip
os.remove(DRIVER_ZIP)
os.remove(DRIVER_LICENSE)
print('DONE!')