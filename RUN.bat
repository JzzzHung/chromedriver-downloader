@ECHO OFF

:: get chrome version
wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value > version.txt

python main.py

DEL /q version.txt

PAUSE