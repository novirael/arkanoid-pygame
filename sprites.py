#-------------------------------------------------------------------------------
# Name:        sprites
# Purpose:
#
# Author:      novirael
#
# Created:     17-04-2012
# Copyright:   (c) novirael 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


from random import randint,choice
import pygame
import math

# Variables
SW, SH = 900, 600


# Define some colors
white = (255,255,255)

# This class represents each block that will get knocked out by the ball
class Kafel(pygame.sprite.Sprite):

   width = 45
   height = 20
   vx = 0
   vy = 6

   # Constructor function
   def __init__(self, img, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface( (self.width, self.height) )
      self.image = pygame.image.load(img).convert()
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

   def update(self, bonus, color, x, y):
      self.drop(bonus, color, x, y)

   def drop(self, bonus, color, x, y):
      if randint(0,10) == 0:
         bon = Bonus(color, x, y, self.vx, self.vy)
         bonus.add(bon)


# This class represens each bonuses dropped by destroyed blocks
class Bonus(pygame.sprite.Sprite):
  def __init__(self, color, x, y, vx, vy):
     pygame.sprite.Sprite.__init__(self)
     self.x, self.y = x, y
     self.vx = vx
     self.vy = vy
     self.image = pygame.Surface( (5,5) )
     pygame.draw.circle(self.image, color, (3,3), 2)
     self.rect = self.image.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y

  def update(self):
     self.y += self.vy
     self.x += self.vx
     self.rect.centerx = self.x
     self.rect.centery = self.y


# This class represents the ball
class Ball(pygame.sprite.Sprite):

    speed = 10.0      # Speed in pixels per cycle
    direction = 50    # Direction of ball (in degrees)
    width = 10        # Surface width
    height = 10       # Surface height

    # Constructor function
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = pos
        self.image = pygame.Surface((self.width, self.height))
        pygame.draw.circle(self.image, white, (5,5), 5 )
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

    # This function will bounce the ball off a horizontal surface (not a vertical one)
    def bounce(self,diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    # Update the position of the ball
    def update(self):

        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)

        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        # Move the image to where our x and y are
        self.rect.x = self.x - 5
        self.rect.y = self.y

        # Do we bounce off the top of the screen?
        if self.y <= 0:
            self.bounce(0)
            self.y = 1

        # Do we bounce off the left of the screen?
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1

        # Do we bounce of the right side of the screen?
        if self.x > SW - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = SW - self.width - 1


# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):

  max_width = 120
  max_height = 10
  # Constructor function
  def __init__(self, p_width, p_height):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface( (p_width, p_height) )
      self.image.fill( (white) )
      self.rect = self.image.get_rect()
      self.rect.topleft = (0, SH - p_height)

  # Update the player
  def update(self, screen, invisibility, p_pos, p_width):
      self.rect.left = p_pos - p_width/2
      #if p_width != 80:
      self.image = pygame.Surface( (p_width, 10) )
      self.image.fill( (white) )
      if self.rect.left < 0:
         self.rect.left = 0
      if self.rect.right > SW:
         self.rect.right = SW
      if not invisibility:
         screen.blit(self.image, (self.rect.left,self.rect.top) )

