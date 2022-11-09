#! /usr/bin/env /usr/bin/python3
#
# This script captures a partial screenshot to outfile.
# On an Apple Mac you may have to allow access for this script to access screen recording
#
#  DOES NOT WORK ON REPLIT because it cannot acces a screen there.
#
# Pull this from git at https://github.com/robyuk/Screenshot to your PC, then install mss on your pc with "pip install mss"
from mss import mss, tools
from time import sleep, strftime

outfileprefix='screenshot'
outfilext='.png'
part={'top':57, 'left':23, 'height':600, 'width':400} # Values are in pixels

timestamp=strftime('%Y%m%d%H%M%S')
outfile=f'{outfileprefix}{timestamp}{outfilext}'
with mss() as screen:
  image=screen.grab(part)
  tools.to_png(image.rgb, image.size, output=outfile)
print(outfile)
