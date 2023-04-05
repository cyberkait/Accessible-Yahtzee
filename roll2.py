from dice import DiceBox
import accessible_output2.outputs.auto
from pygame.locals import *
import pygame
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

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
    o.speak(diceBox.moveLeft())
  elif e.key == pygame.K_RIGHT:
    o.speak(diceBox.moveRight())
  elif e.key == pygame.K_DOWN:
    print ("down")
    o.speak("Down",interrupt=True)
  elif e.key == pygame.K_UP:
    print ("up")
    o.speak("Up",interrupt=True)
  elif e.key == pygame.K_l:
    diceBox.lockDie()
    lock.play()
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
  elif e.key == pygame.K_u:
    diceBox.unlockDie()
    unlock.play()
    return
    
    
    
  else:
    return



while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    # parse commands
    parseKeyDown(event)
