import pygame
from pygame import mixer
from pygame.locals import *
import random
import os
import sys

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

# Define fps
clock = pygame.time.Clock()
fps = 60


screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

# Function to load sound with error handling
def load_sound(file_path):
    if os.path.exists(file_path):
        sound = pygame.mixer.Sound(file_path)
        sound.set_volume(0.20)
        return sound
    else:
        print(f"Error: Sound file '{file_path}' not found.")
        return None

# Load sounds
explosion_fx = load_sound("img/img_explosion.wav")
explosion_fx.set_volume(0.20)

explosion2_fx = load_sound("img/img_explosion2.wav")
explosion2_fx.set_volume(0.20)

laser_fx = load_sound("img/img_laser.wav")
laser_fx.set_volume(0.20)

# Define game variables
rows = 5
cols = 5
alien_cooldown = 1000 #Bullet cooldown in milliseconds
last_alien_shot = pygame.time.get_ticks()


# Define colours
red = (255, 0, 0)
green = (0, 255, 0)


# Load image
bg = pygame.image.load('img/bg.png')

def draw_bg():
	screen.blit(bg, (0, 0))


# Create spaceship class
class Spaceship(pygame.sprite.Sprite):
	def __init__(self, x, y, health):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/spaceship.png')
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.health_start = health
		self.health_remaining = health
		self.last_shot = pygame.time.get_ticks()


	def update(self):
		# Set movement speed
		speed = 8
		# Set a cooldown variable
		cooldown = 500 # Milliseconds

		# Get key press
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.x -= speed
		if key[pygame.K_RIGHT] and self.rect.right < screen_width:
			self.rect.x += speed

		# Record current time
		time_now = pygame.time.get_ticks()
		# Shoot
		if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
			laser_fx.play()
			bullet = Bullets(self.rect.centerx, self.rect.top)
			bullet_group.add(bullet)
			self.last_shot = time_now
			

		# Update mask
		self.mask = pygame.mask.from_surface(self.image)


		# Draw health bar
		pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
		if self.health_remaining > 0:
			pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
		elif self.health_remaining <= 0:
			explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
			explosion_group.add(explosion)
			self.kill()


# Create Bullet class
class Bullets(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/bullet.png')
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		self.rect.y -= 5
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, alien_group, True):
			self.kill()
			explosion_fx.play()
			explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
			explosion_group.add(explosion)




# Create Aliens class
class Aliens(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("img/alien" + str(random.randint(1, 5)) + ".png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.move_counter = 0
		self.move_direction = 1


	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 75:
			self.move_direction *= -1
			self.move_counter *= self.move_direction
		



# Create Alien Bullets class
class Alien_Bullets(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/alien_bullet.png')
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]


	def update(self):
		self.rect.y += 2
		if self.rect.top > screen_height:
			self.kill()
		if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
			self.kill()
			explosion2_fx.play()
			# Reduce spaceship health
			spaceship.health_remaining -= 1
			explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
			explosion_group.add(explosion)


# create Explosion class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []  # Initialize self.images as an empty list
        for num in range(1, 6):
            img = pygame.image.load(f"img/exp{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            elif size == 2:
                img = pygame.transform.scale(img, (40, 40))
            elif size == 3:
                img = pygame.transform.scale(img, (160, 160))
            # Add the image to the list
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 3
        # Update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # If the animation is complete, delete the explosion
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()



# Create sprite groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()


def create_aliens():
	# Generate aliens
	for row in range(rows):
		for item in range(cols):
			alien = Aliens(100 + item * 100, 100 + row * 70)
			alien_group.add(alien)

create_aliens()


# Create player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 3)
spaceship_group.add(spaceship)



run = True
while run:


	clock.tick(fps)

	# Draw background
	draw_bg()

	# Create random alien bullets
	# Record current time 
	time_now = pygame.time.get_ticks()
	#Shoot
	if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
		attacking_alien = random.choice(alien_group.sprites())
		alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
		alien_bullet_group.add(alien_bullet)
		last_alien_shot = time_now




	# Event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# Update spaceship
	spaceship.update()

	# Update sprite group
	bullet_group.update()
	alien_group.update()
	alien_bullet_group.update()
	explosion_group.update()


	# Update sprite groups
	spaceship_group.draw(screen)
	bullet_group.draw(screen)
	alien_group.draw(screen)
	alien_bullet_group.draw(screen)
	explosion_group.draw(screen)


	pygame.display.update()

pygame.quit()