import pygame
import random
from pygame.locals import *
#initialisation, on all pygames
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))
pressed_key = pygame.key.get_pressed()

xpos = 0
ypos = 0
# xpos = random.randint(0,640)
# ypos = random.randint(0,480)
clock = pygame.time.Clock()
rainList = []

class Raindrop:


    def __init__(self):
        self.x = random.randint(0,640)
        self.y = random.randint(0,10)
        self.speed = random.randint(3,8)
        self.size = random.randint(0,10)
        # self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.circle(screen, (169, 162, 160), (self.x, self.y), self.size, self.size)

    def move(self):
        self.y = self.y + self.speed

while 1:
    clock.tick(60)
    screen.fill((88,78,76))

    rainList.append(Raindrop())
    i = 0
    while i < len(rainList):
        rainList[i].move()
        rainList[i].draw()
        if rainList[i].y > 480:
            del rainList[i]
            i -= 1
        i+= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()