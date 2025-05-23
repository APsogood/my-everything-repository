import pygame

#button class
class Button():
    def __init__(self, surface, x, y, image, size_x, size_y):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        # Check if mouse is over the button and handle click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # Always draw the button
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        # Draw a slightly darker outline: from (80, 40, 20) to (70, 35, 15)
        pygame.draw.rect(self.surface, (70, 35, 15), self.rect, 2)
        return action