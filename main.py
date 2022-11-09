#! /usr/bin/env /usr/bin/python3
#
# This script captures a screenshot to outfile every 10 minutes when run on your PC
# On an Apple Mac you may have to allow access for this script to access screen recording
#
#  DOES NOT WORK ON REPLIT because it cannot acces a screen there.
#
# Pull this from git at https://github.com/robyuk/Screenshot to your PC, then install mss on your pc with "pip install mss"
#from mss import mss
from time import sleep, strftime

outfileprefix='screenshot'
outfilext='.png'

while True:
  timestamp=strftime('%Y%m%d%H%M%S')
  with mss() as screen:
    screen.shot(output=f'{outfileprefix}{timestamp}{outfilext}')
  print(f'{outfileprefix}{timestamp}{outfilext}')
  sleep(600)