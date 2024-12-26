import pygame
from pygame.sprite import  Sprite
import random


class Pipe(Sprite):
    qtd_pipe = 2
    velocidade_pipe = 1.5
    velocidade_pipe_original = 1.5
    def __init__(self, screen_rect, base):
        super().__init__()

        self.image_normal = pygame.image.load("images/pipe.png")
        self.rect_image_normal = self.image_normal.get_rect()
        self.rect_image_normal.bottom = base.rect.top

        self.image_invertida = pygame.transform.flip(self.image_normal, False, True)
        self.rect_image_invertida = self.image_invertida.get_rect()
        self.rect_image_invertida.top = screen_rect.top
        self.calcular_pontuacao = True
        

    def adicionar_pipes(self, screen_rect, base, grupo_pipes):
        for i in range(Pipe.qtd_pipe):
            new_pipe = Pipe(screen_rect, base)  
       
            minimo_tamanhoy_pipe = int(screen_rect.bottom * 0.35)
            maximo_tamanhoy_pipe = int(screen_rect.bottom * 0.65)
            tamnho_pipe = random.randint(minimo_tamanhoy_pipe, maximo_tamanhoy_pipe)
            new_pipe.image_normal = pygame.transform.scale(new_pipe.image_normal,
                                                     (new_pipe.rect_image_normal.width, tamnho_pipe))         
            new_pipe.rect_image_normal = new_pipe.image_normal.get_rect()
            new_pipe.rect_image_normal.bottom = screen_rect.bottom   
            new_pipe.image_invertida = pygame.transform.scale(new_pipe.image_invertida,
                                                     (new_pipe.rect_image_normal.width,
                                                        int(new_pipe.rect_image_normal.top - screen_rect.bottom * 0.12)))        
            new_pipe.rect_image_invertida = new_pipe.image_invertida.get_rect()
            new_pipe.rect_image_invertida.top = screen_rect.top


            if i < (Pipe.qtd_pipe - 1): 

                pos_min_image_normal = int(screen_rect.right * 1.1)
                pos_max_image_normal = int(screen_rect.right * 1.30)
                
            else:
                pos_min_image_normal = int(screen_rect.right * 1.70)
                pos_max_image_normal = int(screen_rect.right * 2)
                                

            new_pipe.rect_image_normal.centerx = random.randint(pos_min_image_normal, pos_max_image_normal)
            
            new_pipe.rect_image_invertida.centerx = random.randint(int(new_pipe.rect_image_normal.centerx*0.9),        
                                                                int(new_pipe.rect_image_normal.centerx*1.1))
            # if i < (Pipe.qtd_pipe - 1):
            #     pos_x_first_pipe = new_pipe.rect_image_invertida.right
            
            # else:
            #     if new_pipe.rect_image_invertida.left <= pos_x_first_pipe + new_pipe.rect_image_invertida.width:
            #             new_pipe.rect_image_invertida.left = random.randint(int(pos_x_first_pipe + new_pipe.rect_image_invertida.width),        
            #                                             int(new_pipe.rect_image_normal * 1.15))
            #             print(pos_x_first_pipe * 2)
            #             print(new_pipe.rect_image_invertida.centerx)

            grupo_pipes.add(new_pipe)
            


    def update_pipe(self, grupo_pipe, screen, screen_rect, base):
        for pipe in grupo_pipe:
            pipe.rect_image_normal.right -= pipe.velocidade_pipe
            pipe.rect_image_invertida.right -= pipe.velocidade_pipe

            screen.blit(pipe.image_normal,  pipe.rect_image_normal)
            screen.blit(pipe.image_invertida,  pipe.rect_image_invertida)

            if pipe.rect_image_normal.right <= screen_rect.left and pipe.rect_image_invertida.right <= screen_rect.left:
                grupo_pipe.remove(pipe)
            if len(grupo_pipe) == 1:

                if pipe.rect_image_normal.right >= screen_rect.right / 2 and pipe.rect_image_invertida.right >= screen_rect.right / 2:
                    self.adicionar_pipes(screen_rect, base, grupo_pipe)

    