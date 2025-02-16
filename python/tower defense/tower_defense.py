import pygame as pg
import json
from enemy import Enemy
from world import World
import constants as c
from turret import Turret
from button import Button

# Initialise pygame
pg.init()

# Create clock
clock = pg.time.Clock()

# Create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

# Game variables
placing_turrets = False

# Load images
# Map
map_image = pg.image.load("img/level.png").convert_alpha()
# Individual turret image for mouse cursor
cursor_turret = pg.image.load("img/cursor_turret.png").convert_alpha()
# Enemies
enemy_image = pg.image.load("img/enemy_1.png").convert_alpha()
# Buttons
buy_turret_image = pg.image.load("img/buy_turret.png").convert_alpha()
cancel_image = pg.image.load("img/cancel.png").convert_alpha()

# Load json data for level
with open("level.json") as file:
    world_data = json.load(file)

def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    # Calculate the sequential number of the tile
    mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
    # Check if that tile is grass
    if world.tile_map [mouse_tile_num] == 7:
        # Check that there isn't already a turret there
        space_is_free = True
        for turret in turret_group:
            if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
                space_is_free = False
        # If it is a free space then create turret
        if space_is_free == True:
            new_turret = Turret(cursor_turret, mouse_tile_x, mouse_tile_y)
            turret_group.add(new_turret)

# Create world
world = World(world_data, map_image)
world.process_data()

# Use waypoints from world
waypoints = world.waypoints

# Create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

# Create buttons
turret_button = Button(c.SCREEN_WIDTH + 30, 120, buy_turret_image, True)
cancel_button = Button(c.SCREEN_WIDTH + 50, 180, cancel_image, True)

# Game loop
run = True
while run:

    clock.tick(c.FPS) # 60 FPS

    #########################
    # UPDATING SECTION
    #########################
    
    # Update groups
    enemy_group.update()

    #########################
    # DRAWING SECTION
    ########################

    screen.fill("grey100")

    # Draw level
    world.draw(screen)

    # Draw groups
    enemy_group.draw(screen)
    turret_group.draw(screen)

    # Draw buttons
    # Button for drawing turrets
    if turret_button.draw(screen):
        placing_turrets = True
    # If placing turrets then show the cancel button
    if placing_turrets == True:
        # Show cursor turret
        cursor_rect = cursor_turret.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos

        if cursor_pos[0] <= c.SCREEN_WIDTH:
            screen.blit(cursor_turret, cursor_rect)

        if cancel_button.draw(screen):

            placing_turrets = False
        

    
    # Event handler
    for event in pg.event.get():
        # Quit program
        if event.type == pg.QUIT:
            run = False
        # Mouse click
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            # Check if mouse is on the game area
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                if placing_turrets == True:
                    create_turret(mouse_pos)

    # Update display
    pg.display.flip()


pg.quit()
