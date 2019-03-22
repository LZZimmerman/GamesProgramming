import pygame
import random
import time
import sys
from pygame.locals import *
import math


pygame.mixer.pre_init(44100, -16, 2, 2048) #setup mixer to avoid sound lag
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))
#pygame.font.get_fonts()
#font = pygame.font.Font(None,20)
font = pygame.font.SysFont("arial",20)
pressed_key = pygame.key.get_pressed()
# pygame.mixer.music.load('foo.mp3')
# pygame.mixer.Sound('jump.wav')




clock = pygame.time.Clock()
score = 0
lives = 5

y1 = (lives*20)

while 1:
    clock.tick(60)
    screen.fill((88,78,76))
    screen.blit(font.render("Lives:" + str(lives), True, (0, 0, 0)), (5, 5))
    pressed_key = pygame.key.get_pressed()

    pygame.draw.rect(screen, (200, 0, 50), (10, 30, 30, 100), 2)
    pygame.draw.rect(screen, (200, 0, 50), (10, 30, 30, y1))

    if pressed_key[K_ESCAPE]:
        sys.exit()

    if pressed_key[K_SPACE] and lives > 0:
        lives -= 1

    y1 = (lives * 20)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
           sys.exit()

    pygame.display.update()