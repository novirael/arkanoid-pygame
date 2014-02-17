import math
import pygame
from pygame.locals import *
from sprites import Kafel, Ball, Bonus, Player


kafelek = [ "img/blue.png", "img/green.png", "img/red.png", "img/yellow.png",
"img/purple.png", "img/grey.png" ]
# Colors

color = [(0,100,200), (0,200,0), (255,0,0), (235,235,0), (113,0,185), (200,200,200) ]
black = (0,0,0)
white = (255,255,255)

# Variables
SW, SH = 900, 600
current_level, max_level = 1, 3

k_width, k_height = 45, 20
p_width, p_height = 80,10

p_centerx = SW/2

score = 0
lifes = 5
waiting = 80

level_up, is_moving = False, False
victory, fail = False, False
done = True
collision = False
keyboard_mode = False
zrobione = True

# Functions definitions

# This function deletes sprites off screen
def delete_bad(G):
   for s in G.sprites():
      if s.y < 0 or s.y > SH:
         G.remove(s)

def clear(G):
   for s in G.sprites():
      G.remove(s)

def reset_bonuses():
   global permeability, invisibility, crease, increase, \
   permeability_duration, invisibility_duration, crease_duration, increase_duration, \
   bon_permeability, bon_invisibility, bon_crease, bon_increase
   permeability = False
   invisibility = False
   crease = False
   increase = False
   permeability_duration = 0
   invisibility_duration = 0
   crease_duration = 0
   increase_duration = 0
   clear(bon_permeability)
   clear(bon_invisibility)
   clear(bon_crease)
   clear(bon_increase)

# This function checks the game conditions
def check_game_conditions():
   global current_level, lifes
   global is_moving, victory, fail, level_up
   # Game ends if all the blocks are gone
   if current_level == max_level:
      victory = True
      sound_victory.play()
   if lifes < 1:
      fail = True
      sound_fail.play()
   if len(permeability_blocks) + len(invisibility_blocks) + len(crease_blocks) + len(increase_blocks) + len(other_blocks) == 0  and not level_up:
      level_up = True
      current_level += 1
   if ball.y > SH:
      lifes -= 1
      is_moving = False
      reset_bonuses()

# This function updates the fonts
def update_fonts():
   if done:
      napis = "LEVEL " + str(current_level)  + "    LIFES: " + str(lifes) + \
      "    POINTS: " + str(score)
      screen.blit(font2.render(napis, True, white), (5,5))
      napis = "Permeability: " + str(permeability_duration)
      screen.blit(font2.render(napis, True, white), (300,5))
      napis = "Invisibility: " + str(invisibility_duration)
      screen.blit(font2.render(napis, True, white), (430,5))
      napis = "Crease: " + str(crease_duration)
      screen.blit(font2.render(napis, True, white), (540,5))
      napis = "Increase: " + str(increase_duration)
      screen.blit(font2.render(napis, True, white), (630,5))
   if fail:
      text = font.render("You Fail", True, white)
      textpos = text.get_rect(centerx = background.get_width()/2)
      textpos.top = 300
      screen.blit(text, textpos)
   if victory:
      text = font.render("Congratz! You passed all levels", True, white)
      textpos = text.get_rect(centerx = background.get_width()/2)
      textpos.top = 300
      screen.blit(text, textpos)


def draw_allsprites():
   # Draw blocks
   permeability_blocks.draw(screen)
   invisibility_blocks.draw(screen)
   crease_blocks.draw(screen)
   increase_blocks.draw(screen)
   other_blocks.draw(screen)
   # Draw bonuses
   bon_permeability.draw(screen)
   bon_invisibility.draw(screen)
   bon_crease.draw(screen)
   bon_increase.draw(screen)
   # Draw balls
   balls.draw(screen)

# Countdown function
def czekaj(wait):
   if wait > 0:
      wait -= 1
   return wait

# init
pygame.init()
screen = pygame.display.set_mode([SW, SH])
background = pygame.Surface(screen.get_size())

#pygame.mouse.set_visible(0)

font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 20)

clock = pygame.time.Clock()

# pygame mixer init
pygame.mixer.init()

sound_intro = pygame.mixer.Sound("sounds/start.wav")
sound_victory = pygame.mixer.Sound("sounds/victory.wav")
sound_fail = pygame.mixer.Sound("sounds/fail.wav")
sound_bcollide = pygame.mixer.Sound("sounds/collide-block.wav")
sound_pcollide = pygame.mixer.Sound("sounds/collide-paddle.wav")
sound_bonus = pygame.mixer.Sound("sounds/bonus.wav")

# Create sprite lists
balls = pygame.sprite.Group()
paddles = pygame.sprite.Group()

# Kinds of blocks (colors, bonuses)
permeability_blocks = pygame.sprite.RenderPlain()
invisibility_blocks = pygame.sprite.RenderPlain()
crease_blocks = pygame.sprite.RenderPlain()
increase_blocks = pygame.sprite.RenderPlain()
other_blocks = pygame.sprite.RenderPlain()

# Bonuses
bon_permeability = pygame.sprite.Group()  # Przenikalna kula
bon_invisibility = pygame.sprite.Group()  # Niewidzialna deska
bon_crease = pygame.sprite.Group()        # Zmniejsza deske
bon_increase = pygame.sprite.Group()      # Zwieksza deske

# Bonuses states
permeability = False
invisibility = False
crease = False
increase = False

# Bonuses duration
permeability_duration = 0
invisibility_duration = 0
crease_duration = 0
increase_duration = 0

bonuses = pygame.sprite.RenderPlain()
allblocks = pygame.sprite.RenderPlain()

# Create the player paddle object
player_casual = Player(80, 10)
player_crease = Player(40, 10)
player_increase = Player(120,10)

player = player_casual

# Create the ball
ball = Ball( (p_centerx, 590) )


blocks = [permeability_blocks, invisibility_blocks, crease_blocks,
   increase_blocks, other_blocks]

def draw_level(n):
   top = 80
   left = 100
   global blocks, allblocks
   if n == 1:
      for i in range(4):
         for j in range(15):
            1
            #block = Kafel(kafelek[i], left + j*(k_width+2), top)
            #blocks[i].add(block)
         top += k_height + 2
      for i in range(5):
         for j in range(15):
            block = Kafel(kafelek[i], left + j*(k_width+2), top)
            blocks[i].add(block)
         top += k_height + 2
      for j in range(15):
            block = Kafel(kafelek[4], left + j*(k_width+2), top)
            blocks[4].add(block)
   if n == 2:
      for i in range(4):
         for j in range(15):
            block = Kafel(kafelek[i], left + j*(k_width+2), top)
            blocks[i].add(block)
         top += k_height + 20
      for i in range(4):
         for j in range(15):
            block = Kafel(kafelek[i], left + j*(k_width+2), top)
            blocks[i].add(block)
         top += k_height + 20
      top = 80
      for i in range(20):
         for j in range(2):
            block = Kafel(kafelek[4], 53 + j*(k_width+707), top + i*k_height)
            blocks[4].add(block)

draw_level(1)
sound_intro.play()

# Main program loop
while done:

   wcisniety = pygame.key.get_pressed()

   # Process the events in the game
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = False
      if event.type == MOUSEBUTTONDOWN:
         is_moving = True
      if event.type == KEYDOWN:
         if event.key == K_LSHIFT:
            if keyboard_mode:
               keyboard_mode = False
            else:
               keyboard_mode = True
         if event.key == K_ESCAPE:
            done = False
         if event.key == K_SPACE:
            is_moving = True
         if event.key == K_r:
            p_centerx = SW/2
            lifes = 3
            score = 0
            current_level = 1
            is_moving = False
            victory = False
            fail = False
            reset_bonuses()
            clear(balls)
            permeability_blocks.empty()
            invisibility_blocks.empty()
            crease_blocks.empty()
            increase_blocks.empty()
            other_blocks.empty()
            draw_level(1)
            sound_intro.play()

   # Fill screen
   screen.fill(black)

   # Player position update
   if keyboard_mode:
      if wcisniety[K_LEFT]:
         p_centerx -= 10
      if wcisniety[K_RIGHT]:
         p_centerx += 10
      if p_centerx > SW:
         p_centerx = SW - p_width/2
      if p_centerx < 0:
         p_centerx = p_width/2
   else:
      player_pos = pygame.mouse.get_pos()
      p_centerx = player_pos[0]


   # Update fonts
   update_fonts()

   # Check game condiotions
   if not fail and not victory:

      # Load next level
      if level_up:
         draw_level(current_level)
         sound_intro.play()
         reset_bonuses()
         is_moving = False
         level_up = False

      # When ball isn't moving
      if is_moving == False:
         balls.remove(ball)
         ball = Ball((p_centerx, 590))
         balls.add(ball)
         ball.bounce(130)

      # Player update
      # Crease or increase player paddle
      if crease:
         p_width = 40
         player= player_crease
      if increase:
         p_width = 100
         player = player_increase
      if not crease and not increase:
         p_width = 70
         player = player_casual
      player.update(screen, invisibility, p_centerx, p_width)

      # Balls update
      balls.update()

      # See if the ball hits the player paddle
      if pygame.sprite.spritecollide(player, balls, False):
         diff = (player.rect.left + p_width/2) - (ball.rect.left + ball.width/2)
         ball.rect.top = SH - p_height - ball.height
         ball.bounce(diff)
         sound_pcollide.play()

      # Check for collisions between the balls and the blocks and update blocks
      for b in balls:
         if pygame.sprite.spritecollide(b, permeability_blocks, True):
            permeability_blocks.update(bon_permeability, color[0], b.x, b.y)
            score += 50
            sound_bcollide.play()
            if not permeability:
               b.bounce(0)
         if pygame.sprite.spritecollide(b, invisibility_blocks, True):
            permeability_blocks.update(bon_invisibility, color[1], b.x, b.y)
            score += 40
            sound_bcollide.play()
            if not permeability:
               b.bounce(0)
         if pygame.sprite.spritecollide(b, crease_blocks, True):
            permeability_blocks.update(bon_crease, color[2], b.x, b.y)
            score += 30
            sound_bcollide.play()
            if not permeability:
               b.bounce(0)
         if pygame.sprite.spritecollide(b, increase_blocks, True):
            permeability_blocks.update(bon_increase, color[3], b.x, b.y)
            score += 30
            sound_bcollide.play()
            if not permeability:
               b.bounce(0)
         if pygame.sprite.spritecollide(b, other_blocks, True):
            score += 20
            sound_bcollide.play()
            if not permeability:
               b.bounce(0)

      # Check for collisions between bonuses and player paddle
      if pygame.sprite.spritecollide(player, bon_permeability, True):
         permeability = True
         permeability_duration += waiting
         sound_bonus.play()
      if pygame.sprite.spritecollide(player, bon_invisibility, True):
         invisibility = True
         invisibility_duration += waiting
         sound_bonus.play()
      if pygame.sprite.spritecollide(player, bon_crease, True):
         crease = True
         increase_duration = 0
         crease_duration += waiting
         sound_bonus.play()
      if pygame.sprite.spritecollide(player, bon_increase, True):
         increase = True
         crease_duration = 0
         increase_duration += waiting
         sound_bonus.play()

      # Update bonuses
      bon_permeability.update()
      bon_invisibility.update()
      bon_crease.update()
      bon_increase.update()

      # Counttown
      if permeability_duration > 0:
         permeability_duration -= 1
      if invisibility_duration > 0:
         invisibility_duration -= 1
      if crease_duration > 0:
         crease_duration -= 1
      if increase_duration > 0:
         increase_duration -= 1

      # If time left, change state
      if permeability_duration == 0:
         permeability = False
      if invisibility_duration == 0:
         invisibility = False
      if crease_duration == 0:
         crease = False
      if increase_duration == 0:
         increase = False

      #print "Bonuses:", bonuses, "Pre: ", bon_permeability, "Invi: ", bon_invisibility, "Cre: ", bon_crease, "Incre:", bon_increase

      # Draw all sprites
      draw_allsprites()

      # Limit to 30 fps
      clock.tick(30)

      # Remove sprites off the screen
      delete_bad(balls)
      delete_bad(bon_permeability)
      delete_bad(bon_invisibility)
      delete_bad(bon_crease)
      delete_bad(bon_increase)

      # Check game conditions
      check_game_conditions()

   # Update display
   pygame.display.update()

pygame.display.quit()
pygame.font.quit()
exit()
