import pygame as pg
import json
from enemy import Enemy
from world import World
import constants as c

# Initialise pygame
pg.init()

# Create clock
clock = pg.time.Clock()

# Create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

# Load images
# Map
map_image = pg.image.load("img/level.png").convert_alpha()
# Enemies
enemy_image = pg.image.load("img/enemy_1.png").convert_alpha()

# Load json data for level
with open("level.json") as file:
    world_data = json.load(file)

# Create world
world = World(world_data, map_image)
world.process_data()

# Use waypoints from world
waypoints = world.waypoints

# Create groups
enemy_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

# Game loop
run = True
while run:

    clock.tick(c.FPS) # 60 FPS

    screen.fill("grey100")

    # Draw level
    world.draw(screen)

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