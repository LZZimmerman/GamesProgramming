import pygame
from pygame.locals import *
#initialisation, on all pygames
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))

xpos = 100
ypos = 200
clock = pygame.time.Clock()

while 1:
    pressed_key = pygame.key.get_pressed()

    screen.fill((255,69,0))
    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 10, 2)

    if pressed_key[K_RIGHT] and xpos <= 640:
        xpos += 1
    if pressed_key[K_LEFT]and xpos >= 0:
        xpos -= 1
    if pressed_key[K_UP] and ypos >= 0:
        ypos -= 1
    if pressed_key[K_DOWN] and ypos <= 640:
        ypos += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()