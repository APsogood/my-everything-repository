import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, game_active, winner_message
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Ball collision with left and right walls (scoring)
    if ball.left <= 0:
        player_score += 1
        ball_restart("You got it in!")
    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart("Opponent got it in!")

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Check for win/loss
    if player_score >= 3:
        game_active = False
        winner_message = "You Win!"
    elif opponent_score >= 3:
        game_active = False
        winner_message = "You Lose!"

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart(message):
    global ball_speed_x, ball_speed_y
    # Center the ball and reset speed
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= -1
    ball_speed_y *= -1

    # Display the message for a brief moment
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, light_grey)
    screen.fill(bg_color)
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
    pygame.display.flip()
    pygame.time.delay(1500)

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# Scoring
player_score = 0
opponent_score = 0
game_active = True
winner_message = ""

font = pygame.font.Font(None, 74)

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    if game_active:
        # Ball and paddle movement
        ball_animation()
        player_animation()
        opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Display scores
    player_text = font.render(f"{player_score}", True, light_grey)
    opponent_text = font.render(f"{opponent_score}", True, light_grey)
    screen.blit(player_text, (screen_width / 2 + 20, 20))
    screen.blit(opponent_text, (screen_width / 2 - 50, 20))

    # Display winner message
    if not game_active:
        winner_text = font.render(winner_message, True, light_grey)
        screen.blit(winner_text, (screen_width / 2 - winner_text.get_width() / 2, screen_height / 2 - winner_text.get_height() / 2))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
