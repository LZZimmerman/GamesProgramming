import pygame
import random
import time
from pygame.locals import *
#initialisation, on all pygames
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))
pressed_key = pygame.key.get_pressed()

cloud_image = pygame.image.load("cloud.jpg").convert()
human_image = pygame.image.load("human.png").convert_alpha()
umbrella_image = pygame.image.load("human_umbrella.png").convert_alpha()
# human_image.set_colorkey((255,255,255))
# cloud_image.set_colorkey((255,255,255))
xpos = 0
ypos = 0
# xpos = random.randint(0,640)
# ypos = random.randint(0,480)
clock = pygame.time.Clock()
rainList = []

hxpos = 0
hypos = 288
class Raindrop:


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(3,8)
        self.size = random.randint(0,10)
        # self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.circle(screen, (169, 162, 160), (self.x, self.y), self.size, self.size)

    def move(self):
        self.y = self.y + self.speed


class Cloud:

    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self):
        screen.blit(cloud_image, (self.x, self.y))

    def rain(self):
        rainList.append(Raindrop(random.randint(self.x, self.x+239),211))

    def move(self):
        self.x += 1
        if self.x > 640:
            self.x = -239

class Human:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.openUmbrella = False
    def draw(self):
        screen.blit(human_image, (self.x, self.y))

    def umbrella(self):
         screen.blit(umbrella_image, (self.x, self.y))
        # self.openUmbrella = True


    def move(self):
        pressed_key = pygame.key.get_pressed()
        distance = 2

        if pressed_key[K_RIGHT] and self.x <= 640-170:
            self.x += distance
        if pressed_key[K_LEFT] and self.x >= 0:
            self.x -= distance

    def rained(self, raindrop):
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))
        # self.openUmbrella = True



cloud = Cloud()
human = Human(hxpos,hypos)
# cloud_image.draw()
t = -5
while 1:
    clock.tick(60)
    screen.fill((88,78,76))
    # screen.blit(cloud_image, (100,0))
    cloud.draw()
    cloud.rain()
    cloud.move()
    if time.time() - t > 1:
        human.openUmbrella = False

    if human.openUmbrella == False:
        human.draw()
    else:
        human.umbrella()
    human.move()

    i = 0
    while i < len(rainList):
        rainList[i].move()
        rainList[i].draw()
        if human.rained(rainList[i]):
            human.openUmbrella = True
            t = time.time()
        if rainList[i].y > 480:
            # or human.rained(rainList[i])
            del rainList[i]
            i -= 1
        if human.openUmbrella == True and human.rained(rainList[i]):
           del rainList[i]
           i -= 1
        i+= 1






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()