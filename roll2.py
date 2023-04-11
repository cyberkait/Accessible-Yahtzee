from dice import DiceBox
import accessible_output2.outputs.auto
from pygame.locals import *
import pygame
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import sys

o = accessible_output2.outputs.auto.Auto()
pygame.init()
display = pygame.display.set_mode((300, 300))

roll = pygame.mixer.Sound("sound\dice.wav")
unlock = pygame.mixer.Sound("sound\\unlock.wav")
lock = pygame.mixer.Sound("sound\lock.wav")

diceBox=DiceBox()
def parseKeyDown(e):
  if e.type != pygame.KEYDOWN:
    return

  if e.key == pygame.K_LEFT:
    diceBox.moveLeft()
  elif e.key == pygame.K_RIGHT:
    diceBox.moveRight()
  elif e.key == pygame.K_DOWN:
    diceBox.unlockDie()
    return
  elif e.key == pygame.K_UP:
    diceBox.lockDie()
    return

  elif e.key == pygame.K_s:
    diceBox.changeAnnounceSetting(o.speak)
    return
  
  elif e.key == pygame.K_a:
    o.speak(diceBox.getAllDiceText())
    return 
    
  elif e.key == pygame.K_c:
    o.speak(diceBox.getCurrentDiceText())
    return 
  elif e.key == pygame.K_r:
    diceBox.rollDice()
    roll.play()
    o.speak(diceBox.getAllDiceText())
    return 
  elif e.key == pygame.K_v:
    diceBox.viewScorecard()
    return

    
    
  else:
    return



while True:
  for event in pygame.event.get():
    if event.type == pygame.locals.QUIT:
      pygame.quit()
      sys.exit()

    # parse commands
    parseKeyDown(event)
