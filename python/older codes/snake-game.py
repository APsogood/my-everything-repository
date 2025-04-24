# If you enjoy this snake game, please follow me and give my repository a star!
import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLOCK_SIZE = 20
SNAKE_SPEED = 10

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def display_text(text, color, x, y, font):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def game_over_message():
    screen.fill(BLACK)
    display_text("Game Over!", RED, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, font)
    display_text("Press 'R' to play again or 'Q' to quit.", WHITE, SCREEN_WIDTH // 6, SCREEN_HEIGHT // 2, small_font)
    pygame.display.update()

def generate_food():
    food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return food_x, food_y

def display_score(score):
    display_text("Score: " + str(score), WHITE, 10, 10, small_font)

def game_loop():
    snake_list = []
    snake_length = 1
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2
    snake_direction = RIGHT

    food_x, food_y = generate_food()

    score = 0

    game_over = False
    game_exit = False

    while not game_exit:
        while game_over:
            game_over_message()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_r:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT

        if snake_direction == UP:
            snake_y -= BLOCK_SIZE
        elif snake_direction == DOWN:
            snake_y += BLOCK_SIZE
        elif snake_direction == LEFT:
            snake_x -= BLOCK_SIZE
        elif snake_direction == RIGHT:
            snake_x += BLOCK_SIZE

        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = generate_food()
            snake_length += 1
            score += 10

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        if (snake_x < 0 or snake_x >= SCREEN_WIDTH or
            snake_y < 0 or snake_y >= SCREEN_HEIGHT or
            snake_head in snake_list[:-1]):
            game_over = True

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        draw_snake(snake_list)

        display_score(score)

        pygame.display.update()

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
