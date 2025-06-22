import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, animation_list, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.health = health
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        #select starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self, surface):

        self.update_animation()

        #draw image on screen
        surface.blit(self.image, self.rect)


    def update_animation(self):
        #define animation cooldown
        ANIMATION_COOLDOWN = 50
        #update image depending on current action
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out, reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
