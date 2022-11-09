#! /usr/bin/env /usr/bin/python3
#
# This script captures a screenshot to outfile when run on your PC
# On an Apple Mac you may have to allow access for this script to access screen recording
#
#  DOES NOT WORK ON REPLIT because it cannot acces a screen there.
#
# Pull this from git at https://github.com/robyuk/Screenshot to your PC, then install mss on your pc with "pip install mss"
from mss import mss

outfile='screenshot.png'

with mss() as screen:
  screen.shot(output=outfile)