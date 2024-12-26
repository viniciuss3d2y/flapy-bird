from pygame.sprite import  Sprite
import pygame

class Passarinho(Sprite):
    def __init__(self, screen_rect):
       super().__init__()
        
       self.image =  pygame.image.load("images/bird2.png")                                         
       
       self.rect = self.image.get_rect()
       self.rect.center = screen_rect.center

       self.velocidade_cima = 10
       self.velocidade_baixo = 3.5

       self.gravidade = 0.5
       self.velocidade_max_queda = 10
       self.valor_org_gravidade = 0.5