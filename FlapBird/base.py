
import pygame

class Base:
    velovidade_base = 1.5
    velovidade_base_original = 1.5
    def __init__(self, screen_rect) :

        self.image = pygame.image.load("images/base.png")

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (screen_rect.right, screen_rect.bottom * 0.3))
        self.rect.left = screen_rect.left
        self.rect.bottom = screen_rect.bottom

        