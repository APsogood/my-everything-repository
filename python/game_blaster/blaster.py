import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blaster Game")

# Load assets
# ... (load images, sounds, etc.)
shoot_sound = pygame.mixer.Sound("ding-small-bell.mp3")
winning_sound = pygame.mixer.Sound("winning.mp3")
background = pygame.image.load("grass.jpeg")
player1_image = pygame.image.load("player.png")
player2_image = pygame.image.load("player.png")

# Initialize game variables
player1_pos = [100, 300]
player2_pos = [700, 300]
player1_health = 100
player2_health = 100
player1_score = 0
player2_score = 0
projectiles = []
perks = []
current_perk = None
perk_start_time = 0
start_time = time.time()
fire_rate_multiplier = 1
freeze_player = None
last_shot_time_p1 = 0
last_shot_time_p2 = 0
shot_delay = 0.5  # 0.5 seconds delay between shots
wall_pos = [400, 250]
wall_size = [400, 50]
wall_color = (0, 0, 0, 153)  # RGBA color with 60% opacity
player1_direction = 'right'
player2_direction = 'left'

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)  # 60 FPS

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update game state
        keys = pygame.key.get_pressed()
        handle_movement(keys)
        handle_shooting(keys)
        update_projectiles()
        check_collisions()
        spawn_perks()
        handle_perks()

        # Render the updated game state
        draw_window()

        # Check for round winners
        check_winner()

    pygame.quit()

# Function to handle player movement
def handle_movement(keys):
    global player1_direction, player2_direction
    if freeze_player != 1:
        if keys[pygame.K_w] and player1_pos[1] > 0 and not is_colliding_with_wall(player1_pos, 'up'):
            player1_pos[1] -= 5
            player1_direction = 'up'
        if keys[pygame.K_s] and player1_pos[1] < HEIGHT - 58 and not is_colliding_with_wall(player1_pos, 'down'):
            player1_pos[1] += 5
            player1_direction = 'down'
        if keys[pygame.K_a] and player1_pos[0] > 0 and not is_colliding_with_wall(player1_pos, 'left'):
            player1_pos[0] -= 5
            player1_direction = 'left'
        if keys[pygame.K_d] and player1_pos[0] < WIDTH - 104 and not is_colliding_with_wall(player1_pos, 'right'):
            player1_pos[0] += 5
            player1_direction = 'right'

    if freeze_player != 2:
        if keys[pygame.K_UP] and player2_pos[1] > 0 and not is_colliding_with_wall(player2_pos, 'up'):
            player2_pos[1] -= 5
            player2_direction = 'up'
        if keys[pygame.K_DOWN] and player2_pos[1] < HEIGHT - 58 and not is_colliding_with_wall(player2_pos, 'down'):
            player2_pos[1] += 5
            player2_direction = 'down'
        if keys[pygame.K_LEFT] and player2_pos[0] > 0 and not is_colliding_with_wall(player2_pos, 'left'):
            player2_pos[0] -= 5
            player2_direction = 'left'
        if keys[pygame.K_RIGHT] and player2_pos[0] < WIDTH - 104 and not is_colliding_with_wall(player2_pos, 'right'):
            player2_pos[0] += 5
            player2_direction = 'right'

def is_colliding_with_wall(player_pos, direction):
    player_width, player_height = 104, 58  # Player image size
    if direction == 'up' and player_pos[1] - 5 < wall_pos[1] + wall_size[1] and player_pos[1] > wall_pos[1] and player_pos[0] + player_width > wall_pos[0] and player_pos[0] < wall_pos[0] + wall_size[0]:
        return True
    if direction == 'down' and player_pos[1] + player_height + 5 > wall_pos[1] and player_pos[1] < wall_pos[1] + wall_size[1] and player_pos[0] + player_width > wall_pos[0] and player_pos[0] < wall_pos[0] + wall_size[0]:
        return True
    if direction == 'left' and player_pos[0] - 5 < wall_pos[0] + wall_size[0] and player_pos[0] > wall_pos[0] and player_pos[1] + player_height > wall_pos[1] and player_pos[1] < wall_pos[1] + wall_size[1]:
        return True
    if direction == 'right' and player_pos[0] + player_width + 5 > wall_pos[0] and player_pos[0] < wall_pos[0] + wall_size[0] and player_pos[1] + player_height > wall_pos[1] and player_pos[1] < wall_pos[1] + wall_size[1]:
        return True
    return False

def is_projectile_colliding_with_wall(projectile_pos, direction):
    if direction == 'up' and projectile_pos[1] - 5 < wall_pos[1] + wall_size[1] and projectile_pos[1] > wall_pos[1] and projectile_pos[0] + 5 > wall_pos[0] and projectile_pos[0] < wall_pos[0] + wall_size[0]:
        return True
    if direction == 'down' and projectile_pos[1] + 5 > wall_pos[1] and projectile_pos[1] < wall_pos[1] + wall_size[1] and projectile_pos[0] + 5 > wall_pos[0] and projectile_pos[0] < wall_pos[0] + wall_size[0]:
        return True
    if direction == 'left' and projectile_pos[0] - 5 < wall_pos[0] + wall_size[0] and projectile_pos[0] > wall_pos[0] and projectile_pos[1] + 5 > wall_pos[1] and projectile_pos[1] < wall_pos[1] + wall_size[1]:
        return True
    if direction == 'right' and projectile_pos[0] + 5 > wall_pos[0] and projectile_pos[0] < wall_pos[0] + wall_size[0] and projectile_pos[1] + 5 > wall_pos[1] and projectile_pos[1] < wall_pos[1] + wall_size[1]:
        return True
    return False

# Function to handle shooting
def handle_shooting(keys):
    global last_shot_time_p1, last_shot_time_p2
    current_time = time.time()
    effective_shot_delay = shot_delay / fire_rate_multiplier  # Apply fire rate multiplier
    if keys[pygame.K_f] and current_time - last_shot_time_p1 > effective_shot_delay:
        for _ in range(fire_rate_multiplier):  # Fire multiple projectiles if fire rate is increased
            if player1_direction == 'right':
                projectiles.append({'pos': [player1_pos[0] + 104, player1_pos[1] + 40], 'dir': 'right'})
            elif player1_direction == 'left':
                projectiles.append({'pos': [player1_pos[0], player1_pos[1] + 20], 'dir': 'left'})
            elif player1_direction == 'up':
                projectiles.append({'pos': [player1_pos[0] + 42, player1_pos[1]], 'dir': 'up'})
            elif player1_direction == 'down':
                projectiles.append({'pos': [player1_pos[0] + 20, player1_pos[1] + 58], 'dir': 'down'})
        shoot_sound.play()
        last_shot_time_p1 = current_time
    if keys[pygame.K_SLASH] and current_time - last_shot_time_p2 > effective_shot_delay:
        for _ in range(fire_rate_multiplier):  # Fire multiple projectiles if fire rate is increased
            if player2_direction == 'right':
                projectiles.append({'pos': [player2_pos[0] + 104, player2_pos[1] + 40], 'dir': 'right'})
            elif player2_direction == 'left':
                projectiles.append({'pos': [player2_pos[0], player2_pos[1] + 20], 'dir': 'left'})
            elif player2_direction == 'up':
                projectiles.append({'pos': [player2_pos[0] + 42, player2_pos[1]], 'dir': 'up'})
            elif player2_direction == 'down':
                projectiles.append({'pos': [player2_pos[0] + 20, player2_pos[1] + 58], 'dir': 'down'})
        shoot_sound.play()
        last_shot_time_p2 = current_time

# Function to update projectile positions and check for collisions
def update_projectiles():
    for projectile in projectiles:
        if projectile['dir'] == 'right':
            projectile['pos'][0] += 10
        elif projectile['dir'] == 'left':
            projectile['pos'][0] -= 10
        elif projectile['dir'] == 'up':
            projectile['pos'][1] -= 10
        elif projectile['dir'] == 'down':
            projectile['pos'][1] += 10

        if projectile['pos'][0] < 0 or projectile['pos'][0] > WIDTH or projectile['pos'][1] < 0 or projectile['pos'][1] > HEIGHT:
            projectiles.remove(projectile)
        elif is_projectile_colliding_with_wall(projectile['pos'], projectile['dir']):
            projectiles.remove(projectile)

# Function to check for collisions between projectiles and players
def check_collisions():
    global player1_health, player2_health
    player_width, player_height = 104, 58  # Player image size
    for projectile in projectiles:
        if projectile['dir'] == 'right' and player2_pos[0] < projectile['pos'][0] < player2_pos[0] + player_width and player2_pos[1] < projectile['pos'][1] < player2_pos[1] + player_height:
            player2_health -= 5
            projectiles.remove(projectile)
        elif projectile['dir'] == 'left' and player1_pos[0] < projectile['pos'][0] < player1_pos[0] + player_width and player1_pos[1] < projectile['pos'][1] < player1_pos[1] + player_height:
            player1_health -= 5
            projectiles.remove(projectile)
        elif projectile['dir'] == 'up' and player2_pos[1] < projectile['pos'][1] < player2_pos[1] + player_height and player2_pos[0] < projectile['pos'][0] < player2_pos[0] + player_width:
            player2_health -= 5
            projectiles.remove(projectile)
        elif projectile['dir'] == 'down' and player1_pos[1] < projectile['pos'][1] < player1_pos[1] + player_height and player1_pos[0] < projectile['pos'][0] < player1_pos[0] + player_width:
            player1_health -= 5
            projectiles.remove(projectile)
        elif projectile['dir'] == 'right' and player1_pos[0] < projectile['pos'][0] < player1_pos[0] + player_width and player1_pos[1] < projectile['pos'][1] < player1_pos[1] + player_height:
            player1_health -= 5
            projectiles.remove(projectile)
        elif projectile['dir'] == 'left' and player2_pos[0] < projectile['pos'][0] < player2_pos[0] + player_width and player2_pos[1] < projectile['pos'][1] < player2_pos[1] + player_height:
            player2_health -= 5
            projectiles.remove(projectile)
        elif projectile['dir'] == 'up' and player1_pos[1] < projectile['pos'][1] < player1_pos[1] + player_height and player1_pos[0] < projectile['pos'][0] < player1_pos[0] + player_width:
            player1_health -= 5
            projectiles.remove(projectile)
        elif projectile['dir'] == 'down' and player2_pos[1] < projectile['pos'][1] < player2_pos[1] + player_height and player2_pos[0] < projectile['pos'][0] < player2_pos[0] + player_width:
            player2_health -= 5
            projectiles.remove(projectile)

# Function to spawn and handle perks
def spawn_perks():
    if random.randint(1, 100) == 1:
        perks.append({'pos': [random.randint(0, WIDTH), random.randint(0, HEIGHT)], 'type': random.choice(['randomPotion', 'increaseFireRate', 'freeze'])})

def handle_perks():
    global player1_health, player2_health, current_perk, perk_start_time, fire_rate_multiplier, freeze_player
    for perk in perks:
        if player1_pos[0] < perk['pos'][0] < player1_pos[0] + 50 and player1_pos[1] < perk['pos'][1] < player1_pos[1] + 50:
            apply_perk(perk, 1)
            current_perk = perk['type']
            perk_start_time = time.time()
            perks.remove(perk)
        elif player2_pos[0] < perk['pos'][0] < player2_pos[0] + 50 and player2_pos[1] < perk['pos'][1] < player2_pos[1] + 50:
            apply_perk(perk, 2)
            current_perk = perk['type']
            perk_start_time = time.time()
            perks.remove(perk)

    # Reset perks after 5 seconds
    if current_perk and time.time() - perk_start_time > 5:
        current_perk = None
        fire_rate_multiplier = 1
        freeze_player = None

def apply_perk(perk, player):
    global player1_health, player2_health, fire_rate_multiplier, freeze_player
    if perk['type'] == 'randomPotion':
        if player == 1:
            player2_health -= 50
        else:
            player1_health -= 50
    elif perk['type'] == 'increaseFireRate':
        fire_rate_multiplier = 5
    elif perk['type'] == 'freeze':
        freeze_player = 2 if player == 1 else 1

# Function to draw players, projectiles, and perks on the screen
def draw_window():
    win.blit(background, (0, 0))  # Draw the background
    rotated_player1_image = pygame.transform.rotate(player1_image, get_rotation_angle(player1_direction))
    rotated_player2_image = pygame.transform.rotate(player2_image, get_rotation_angle(player2_direction))
    win.blit(rotated_player1_image, player1_pos)  # Draw player 1
    win.blit(rotated_player2_image, player2_pos)  # Draw player 2
    
    # Draw the wall with 60% opacity
    wall_surface = pygame.Surface(wall_size, pygame.SRCALPHA)
    wall_surface.fill(wall_color)
    win.blit(wall_surface, wall_pos)
    
    for projectile in projectiles:
        pygame.draw.circle(win, (255, 255, 255), projectile['pos'], 5)
    for perk in perks:
        pygame.draw.circle(win, (0, 255, 0), perk['pos'], 10)
    
    # Display player status
    display_status()
    
    pygame.display.update()

def get_rotation_angle(direction):
    if direction == 'up':
        return 90
    elif direction == 'down':
        return -90
    elif direction == 'left':
        return 180
    elif direction == 'right':
        return 0
    return 0

def display_status():
    font = pygame.font.SysFont(None, 24)
    elapsed_time = int(time.time() - start_time)
    
    player1_status1 = f"Player 1 Health: {player1_health}"
    player1_status2 = f"Wins: {player1_score}"
    player2_status1 = f"Player 2 Health: {player2_health}"
    player2_status2 = f"Wins: {player2_score}"
    middle_status1 = f"Current Perk: {current_perk}"
    middle_status2 = f"Time Elapsed: {elapsed_time}s"
    
    text1_1 = font.render(player1_status1, True, (255, 255, 255))
    text1_2 = font.render(player1_status2, True, (255, 255, 255))
    text2_1 = font.render(player2_status1, True, (255, 255, 255))
    text2_2 = font.render(player2_status2, True, (255, 255, 255))
    text_middle1 = font.render(middle_status1, True, (255, 255, 255))
    text_middle2 = font.render(middle_status2, True, (255, 255, 255))
    
    win.blit(text1_1, (10, 10))
    win.blit(text1_2, (10, 30))
    win.blit(text_middle1, (WIDTH // 2 - text_middle1.get_width() // 2, 10))
    win.blit(text_middle2, (WIDTH // 2 - text_middle2.get_width() // 2, 30))
    win.blit(text2_1, (WIDTH - text2_1.get_width() - 10, 10))
    win.blit(text2_2, (WIDTH - text2_2.get_width() - 10, 30))

# Function to check for round winners and update scores
def check_winner():
    global player1_health, player2_health, player1_score, player2_score
    if player1_health <= 0:
        player2_score += 1
        reset_round()
    elif player2_health <= 0:
        player1_score += 1
        reset_round()

    if player1_score == 5:
        display_winner("Player One wins the game!")
    elif player2_score == 5:
        display_winner("Player Two wins the game!")

def display_winner(message):
    font = pygame.font.SysFont(None, 48)
    text = font.render(message, True, (255, 255, 255))
    win.fill((0, 0, 0))
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    winning_sound.play()
    time.sleep(3)
    pygame.quit()
    exit()

def reset_round():
    global player1_health, player2_health, projectiles, perks, current_perk, fire_rate_multiplier, freeze_player
    player1_health = 100
    player2_health = 100
    projectiles = []
    perks = []
    current_perk = None
    fire_rate_multiplier = 1
    freeze_player = None

if __name__ == "__main__":
    main()
