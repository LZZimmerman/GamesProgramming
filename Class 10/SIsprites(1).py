import pygame, random, time
from pygame.locals import *

		# PYGAME SETUP AND INITIALISATION
pygame.init()

# -- Global constants
 
# COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Space Invaders with Sprites!")
clock = pygame.time.Clock()

# Loading images and converting where appropriate
img1 = pygame.image.load("fighter.png")
img1.set_colorkey((255,255,255))
img2 = pygame.image.load("invader.png").convert_alpha()
img3 = pygame.image.load("missile.png").convert_alpha()

explosions = []

for i in range(9):
	filename = 'regularExplosion0{}.png'.format(i)
	explosion_image = pygame.image.load(filename).convert()
	explosion_image.set_colorkey(BLACK)
	exp_img = pygame.transform.scale(explosion_image, (32,32))
	explosions.append(exp_img)

		## CLASS DECLEARATIONS (AKA BLUEPRINTS) ##

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = img1
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREEN_WIDTH / 2
		self.rect.bottom = SCREEN_HEIGHT - self.rect.y - 2
		self.speedx = 3

	def update(self):
		self.speedx = 0
		self.speedy = 0
		keystate = pygame.key.get_pressed()

		if keystate[K_LEFT]:
			self.speedx = -5
		if keystate[K_RIGHT]:
			self.speedx = 5
		if keystate[K_UP]:
			self.speedy = -5
		if keystate[K_DOWN]:
			self.speedy = 5

		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.bottom > SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT
		if self.rect.top < 0:
			self.rect.top = 0

	def fire(self):
		m = Missiles(self.rect.centerx, self.rect.top)
		bullets.add(m)
		all_sprites_list.add(m)


class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = img2
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(25,775)
		self.rect.y = 0
		self.yspeed = random.randint(1,2)
		self.xspeed = random.randint(-2,2)

	def update(self):
		self.rect.y += self.yspeed
		self.rect.x += self.xspeed

		if self.rect.top > SCREEN_HEIGHT:
			self.rect.x = random.randint(0,800)
			self.rect.y = 0
			self.yspeed = random.randint(1,2)
			self.xspeed = random.randint(-2,2)

		if self.rect.right > 800 or self.rect.left < 0:
			self.xspeed *= -1

class Missiles(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = img3
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = x-6
		self.rect.y = y
		self.yspeed = -2

	def update(self):
		self.rect.y += self.yspeed

		if self.rect.top < 0:
			self.kill()

	# def explode(self):
	# 	Explosion(self.rect.x, self.rect.y)

class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = explosions[0]
		self.index = 0
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.currentframe = 0
		self.framesBetween = 5
	def update(self):
		self.currentframe += 1
		if self.currentframe >= self.framesBetween:
			self.image = explosions[self.index]
			self.index += 1
			self.currentframe = 0
			if self.index == 8:
				self.kill()


## INSTANTIATIONS / GLOBAL VARIABLES

player = Player()


all_sprites_list = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites_list.add(player)
 

for i in range(6):
	e = Enemy()
	enemies.add(e)
	all_sprites_list.add(e)


gameOn = True


				## MAIN LOOP
while gameOn:

	clock.tick(50)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOn = False
		elif event.type == pygame.KEYDOWN: ##Checks once per loop if player presses space rather than continuously
			if event.key == K_SPACE:
				player.fire()

	keystate = pygame.key.get_pressed()

	# if keystate[K_SPACE]:
	# 	player.fire()



	all_sprites_list.update()
	enemies.update()
	bullets.update()
	
	#if pygame.sprite.spritecollide(player, enemies, True): ##destroys the second object
		()
	# 	gameOn = False

	hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
	for hit in hits:
		m = Explosion(hit.rect.x, hit.rect.y)
		all_sprites_list.add(m)

		e = Enemy()
		enemies.add(e)
		all_sprites_list.add(e)


	screen.fill(BLACK)
	all_sprites_list.draw(screen)

	pygame.display.flip()









