import pygame as pg
from enemy import Enemy
import constants as c

# Initialise pygame
pg.init()

# Create clock
clock = pg.time.Clock()

# Create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

# Load images
enemy_image = pg.image.load("img/enemy_1.png").convert_alpha()

# Create groups
enemy_group = pg.sprite.Group()

enemy = Enemy((200, 300), enemy_image)
enemy_group.add(enemy)

# Game loop
run = True
while run:

    clock.tick(c.FPS) # 60 FPS

    screen.fill("grey100")

    # Update groups
    enemy_group.update()

    # Draw groups
    enemy_group.draw(screen)
    
    # Event handler
    for event in pg.event.get():
        # Quit program
        if event.type == pg.QUIT:
            run = False

    # Update display
    pg.display.flip()


pg.quit()