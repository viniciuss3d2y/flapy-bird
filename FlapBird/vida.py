import pygame
from time import time


class loopinterrompido(Exception):
    pass  




class Vida():
    def __init__(self, screen_rect):
       
   
        # imagens da vida do player
       self.vida_cheia = pygame.image.load('images/vida_cheia.png')
       self.vida_menos_um = pygame.image.load('images/vida-1.png')
       self.vida_menos_dois = pygame.image.load('images/vida-2.png')
       self.vida_menos_tres = pygame.image.load('images/vida-3.png')
       self.vida_menos_quatro = pygame.image.load('images/vida-4.png')
       self.vida_menos_cinco = pygame.image.load('images/vida-5.png')
       
       
       self.image = self.vida_cheia
       self.rect = self.image.get_rect()

       self.rect.top = screen_rect.top + 10
       self.rect.right = screen_rect.right - 50

       self.total_vidas = 5
        # tem po para para auxiliar nas colisoes dos inimigos e personagem
        # para que a vida nao esvazie imediatamente com a colisao
       self.tempo_colisao = time()

       # imagem que vai aparecer quando o player perder uma vida
       self.menos_vida = pygame.image.load('images/perde_vida.png')
       self.menos_vida = pygame.transform.scale(self.menos_vida, (70, 70))
       self.menos_vida_rect = self.menos_vida.get_rect()
       self.menos_vida_rect.center = screen_rect.center
       
       self.time_draw_menos_vida = 1
       self.draw_menos_vida = False

    
    
    def check_vida(self,grupo_pipes, passarinho, screen, screen_rect, base):
        tempo_atual = time()


        if int(tempo_atual) - int(self.tempo_colisao) >= 2:
            verificar_colisao = True
            for pipe in grupo_pipes:                            #passarinho.rect.colliderect(pipe.rect_image_invertida) or  passarinho.rect.colliderect(pipe.rect_image_normal)

                passarinho_mask = pygame.mask.from_surface(passarinho.image)
                pipe_invertido_mask = pygame.mask.from_surface(pipe.image_invertida)
                pipe_normal_mask = pygame.mask.from_surface(pipe.image_normal)
                distancia_pipe_invertido = (round(pipe.rect_image_invertida.x) - round(passarinho.rect.x), round(pipe.rect_image_invertida.y) - round(passarinho.rect.y))
                distancia_pipe_normal = (round(pipe.rect_image_normal.x) - round(passarinho.rect.x), round(pipe.rect_image_normal.y) - round(passarinho.rect.y))

                if passarinho_mask.overlap(pipe_invertido_mask, distancia_pipe_invertido) or passarinho_mask.overlap(pipe_normal_mask, distancia_pipe_normal) or  passarinho.rect.top <= screen_rect.top or passarinho.rect.bottom >= base.rect.top:
                    if verificar_colisao:                                               
                        self.total_vidas -= 1
                        self.tempo_colisao = tempo_atual
                        self.time_draw_menos_vida = time()
                        verificar_colisao = False

        if int(time()) - int(self.time_draw_menos_vida) <= 1 :
            screen.blit(self.menos_vida, self.menos_vida_rect) 

    
    def draw_vida(self, screen):
        if self.total_vidas == 5:
            screen.blit(self.vida_cheia, self.rect)
        elif self.total_vidas == 4:
            screen.blit(self.vida_menos_um, self.rect)
        elif self.total_vidas == 3 :
            screen.blit(self.vida_menos_dois, self.rect)
        elif self.total_vidas == 2 :
            screen.blit(self.vida_menos_tres, self.rect)
        elif self.total_vidas == 1 :
            screen.blit(self.vida_menos_quatro, self.rect)
        elif self.total_vidas <= 0:
            screen.blit(self.vida_menos_cinco, self.rect)
            
                                            
    

    def check_died(self, passarinho, screen_rect, score, grupo_pipes, pipe, base1, base2):

        if self.total_vidas <= 0:

            passarinho.rect.center = screen_rect.center
            self.total_vidas = 5
            # se o jogador morrer soma o xp que ele ganhou nesta partida com o seu nivel 
            with open('nivel_player.txt', 'r') as arquivo:
                conteudo = arquivo.read()
            # soma o xp ganho na partida com o nivel
            novo_nivel = float(conteudo) + score.nivel_player
            with open('nivel_player.txt', 'w') as arquivinho:
                arquivinho.write(str(novo_nivel))
            # verifica se a o jogador bateu seu record
            # se o jogador morrer sua pontuaçao zera
            score.check_max_score()
            score.score = 0
            # o xp adiquirido nesta parida tambem é zerados após ser adicionado ao seu nivel
            score.nivel_player = 0
            grupo_pipes.empty()
            pipe.velocidade_pipe = pipe.velocidade_pipe_original
            base1.velovidade_base = base1.velovidade_base_original

            base1.rect.left = screen_rect.left
            base2.rect.left = base1.rect.right 
            
            
            

            



