import pygame, sys, random, math, time
from pygame.locals import *

# pygame.mixer.pre_init(44100, -16, 2, 2048)

pygame.init()
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

background = pygame.image.load('background.gif')

# This function will create a display Surface
screen = pygame.display.set_mode((800,400))

spaceship = pygame.image.load("spaceship.png").convert_alpha()
enemy_image1 = pygame.image.load("invader.jpg").convert()
enemy_image = pygame.transform.scale(enemy_image1, (35,35))

last_time_enemy_spawned = 0
time_since_last_shot = 0
BLACK = (0, 0, 0)

score = 0
lives = 4



class Enemies:

	def __init__(self):
		self.x = random.randint(0,800)
		self.y = -40
		self.dx = 1

	def move(self):
		self.y += 2
		# self.x += self.dx

	def bounce(self):
		if self.x < 0 or self.x > 775:
			self.dx = -1

	def draw(self):
		screen.blit(enemy_image, (self.x, self.y))

	def hit_by(self, missile):
		return pygame.Rect(self.x, self.y, 35, 35).collidepoint((missile.x, missile.y)) 


class Fighter:

	def __init__(self):
		self.x = 400
		self.y = 330
		self.lives = 5
		self.angle = 0

	def draw(self):
		screen.blit(spaceship, (self.x, self.y))

	def fire(self):
		missiles.append(Missile(self.x + spaceship.get_width()/2))

	def move(self):
		if pressed_keys[K_RIGHT] and self.x<750:
			self.x += 5
		if pressed_keys[K_LEFT] and self.x>0:
			self.x -= 5

	def hit_by(self,enemy):
		return pygame.Rect(self.x, self.y, 50,50).colliderect(enemy.x, enemy.y, 40,30)


class Missile:

	def __init__(self, x):
		self.x = x
		self.y = 350

	def draw(self):
		pygame.draw.line(screen, (255,0,0), (self.x,self.y), (self.x, self.y - 4), 1) 

	def move(self):
		self.y -= 10


enemies = []
missiles = []

fighter = Fighter()


while 1:
	clock.tick(60)
	# EXIT PROCESS
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[K_ESCAPE]:
		sys.exit()

	
	# RENDER PROCESS
	screen.fill(BLACK)
	
	#rollingBackgrd()

	
	if time.time() - last_time_enemy_spawned > 0.8:
		enemies.append(Enemies())
		last_time_enemy_spawned = time.time()

	if pressed_keys[K_SPACE] and time.time() - time_since_last_shot > 0.2:
		fighter.fire()
		time_since_last_shot = time.time()

	fighter.move()
	fighter.draw()

	m=0
	while m < len(missiles):
		missiles[m].move()
		missiles[m].draw()

		if missiles[m].y < -4:
			del missiles[m]
			m -= 1

		m += 1

	e = 0
	while e < len(enemies):
		enemies[e].move()		
		enemies[e].draw()
		enemies[e].bounce()
		
		if enemies[e].y > 400:
			del enemies[e]
			e -= 1
		
		if fighter.hit_by(enemies[e]):
			if lives > 1:
				del enemies[e]
				lives -= 1
				e -= 1
			else:
				sys.exit()

		j = 0
		while j < len(missiles):
			if enemies[e].hit_by(missiles[j]):
				del enemies[e]
				del missiles[j]
				e -= 1
				break
			j+=1

		e += 1
	 
	
	pygame.display.flip() 

