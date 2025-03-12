#import libraries
import pygame
import random

#initialise pygame
pygame.init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumpy")

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0

#define colours
WHITE = (255, 255, 255)

#load images
jumpy_image = pygame.image.load("Jumpy/assets/jump.png").convert_alpha()
bg_image = pygame.image.load("Jumpy/assets/bg.png").convert_alpha()
platform_image = pygame.image.load('Jumpy/assets/pads/wood.png').convert_alpha()

#function for drawing the background
def draw_bg(bg_scroll):
    screen.blit(bg_image, (0, 0 + bg_scroll))
    screen.blit(bg_image, (0, -600 + bg_scroll))


#player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        #reset variables
        scroll = 0
        dx = 0
        dy = 0

        #process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
           dx = -10
           self.flip = True
        if key[pygame.K_d]:
           dx = 10
           self.flip = False

        #gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #ensure player doesn't go off the edge of the screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right


        #check collision with platforms
        for platform in platform_group:
            #collision in the y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if above the platform
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20

        
        #check collision with ground
        if self.rect.bottom + dy > SCREEN_HEIGHT:
            dy = 0
            self.vel_y = -20


        #check if the player has bounced to the top of the screen
        if self.rect.top <= SCROLL_THRESH:
            #if player is jumping
            if self.vel_y < 0:
                scroll = -dy

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 10, self.rect.y - 5))
        pygame.draw.rect(screen, WHITE, self.rect, 2)



#platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        
        #update platform's vertical position
        self.rect.y += scroll


#player instance
jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

#create sprite groups
platform_group = pygame.sprite.Group()

#create temporary platforms
for p in range(MAX_PLATFORMS):
    p_w = random.randint(40, 60)
    p_x = random.randint(0, SCREEN_WIDTH - p_w)
    p_y = p * random.randint(80, 120)
    platform = Platform(p_x, p_y, p_w)
    platform_group.add(platform)


#game loop
run = True
while run:

    clock.tick(FPS)

    scroll = jumpy.move()

    #draw background
    bg_scroll += scroll
    if bg_scroll >= 600:
        bg_scroll = 0
    draw_bg(bg_scroll)

    #draw temporary scroll threshold
    pygame.draw.line(screen, WHITE, (0, SCROLL_THRESH), (SCREEN_WIDTH, SCROLL_THRESH))

    #update platforms
    platform_group.update(scroll)

    #draw sprites
    platform_group.draw(screen)
    jumpy.draw()


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

pygame.quit()
