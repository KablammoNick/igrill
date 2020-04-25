import json
import time
import requests

from igrill import IGrillV2Peripheral

ADDRESS = 'D4:81:CA:23:67:A1'
INTERVAL = 15
URL = 'https://your-api/bbq/'

if __name__ == '__main__':
 periph = IGrillV2Peripheral(ADDRESS)
 while True:
  temperature=periph.read_temperature()
  # Probe 1
  if temperature[1] != 63536.0:
   mytemp = {'probe1': temperature[1]}
   requests.post(url, data = mytemp)

  # Probe 2
  if temperature[2] != 63536.0:
   mytemp = {'probe1': temperature[2]}
   requests.post(url, data = mytemp)

  # Probe 3
  if temperature[3] != 63536.0:
   mytemp = {'probe1': temperature[3]}
   requests.post(url, data = mytemp)

  # Probe 4
  if temperature[4] != 63536.0:
   mytemp = {'probe1': temperature[4]}
   requests.post(url, data = mytemp)
   
  # Battery
  mybattery = {'batter': periph.read_battery()}
  requests.post(url, data = mytemp)

  time.sleep(INTERVAL)
