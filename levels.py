#-------------------------------------------------------------------------------
# Name:        levels
# Purpose:
#
# Author:      novirael
#
# Created:     17-04-2012
# Copyright:   (c) novirael 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Import
from sprites import Kafel

# Blocks
kafelek = [ "img/blue.png", "img/green.png", "img/red.png", "img/yellow.png",
"img/grey.png", "img/purple.png" ]

# Colors
black = (0,0,0)
white = (255,255,255)
blue = (0,100,200)
green = (0,200,0)
red = (255,0,0)
yellow = (235,235,0)
purple = (113,0,185)

# Variables
SW, SH = 900, 600
k_width, k_height = 45, 20

def draw_level(n):
   if n == 1:
      # The top of the block (y position)
      top = 80
      for i in range(15):
         block = Kafel(blue, kafelek[0], i*(k_width+2), top)
         blocks.add(block)
         allsprites.add(block)
      return allsprites, blocks

      # --- Create blocks
      """
# Five rows of blocks
for row in range(2):
    for column in range(0,20):
        block = Kafel(blue, kafelek[0], column*(k_width+2), top)
        blocks.add(block)
        allsprites.add(block)
    # Move the top of the next row down
    top += k_height + 2
"""

