import pygame
from passarinho import Passarinho
from base import Base
import time
from pipe import Pipe
from pygame.sprite import Group
from score import Score
from vida import Vida
import sys
from funcoes_game import update_velocidade_jogo


def run_game():

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption('mata pombo')
    screen_rect = screen.get_rect()
    
    score = Score()
    my_passarinho = Passarinho(screen_rect)
    imagens_passarinho = [pygame.image.load("images/bird1.png"), 
                                 pygame.image.load("images/bird2.png"),
                                 pygame.image.load("images/bird3.png")]
    vida = Vida(screen_rect)
    base1 = Base(screen_rect)
    base2 = Base(screen_rect)
    base2.rect.left = base1.rect.right
    pipe = Pipe(screen_rect, base1)
    # grupo de sprite pipe
    grupo_pipes = Group()
    # grupo de sprite passarinho
    grupo_passarinho = Group()
    grupo_passarinho.add(my_passarinho)
    # adicionar pipoes
    pipe.adicionar_pipes(screen_rect, base1, grupo_pipes)

    # auxiliar alternar imagem passaro
    tempo_inicio = time.time()
    mover_passaro_cima = False
    imagem_fundo = pygame.image.load("images/bg.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo,
                                         (int(screen_rect.right), int(screen_rect.bottom)))

    # pausar o jogo
    game_activation = True
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if game_activation:
                        game_activation = False
                    else:
                        game_activation = True

                elif event.key == pygame.K_SPACE:
                    mover_passaro_cima = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    mover_passaro_cima = False

        # movimentacao do passarinho
        if game_activation:
            if mover_passaro_cima and my_passarinho.rect.top > screen_rect.top:
                my_passarinho.rect.top -= my_passarinho.velocidade_cima
                my_passarinho.gravidade = my_passarinho.valor_org_gravidade
            else:
                if my_passarinho.rect.bottom < base1.rect.top:
                    if my_passarinho.gravidade >= my_passarinho.velocidade_max_queda:
                        my_passarinho.gravidade = my_passarinho.velocidade_max_queda
                    my_passarinho.rect.top += my_passarinho.gravidade
                    my_passarinho.gravidade += my_passarinho.valor_org_gravidade
                    
                
            # mover base
            base1.rect.right -= base1.velovidade_base
            base2.rect.right -= base1.velovidade_base
            if base1.rect.right < screen_rect.left:
                base1.rect.left = base2.rect.right

            elif base2.rect.right < screen_rect.left:
                base2.rect.left = base1.rect.right
           
            screen.fill((255, 255, 155))
            screen.blit(imagem_fundo, (0, 0))
            pipe.update_pipe(grupo_pipes, screen, screen_rect, base1)
            screen.blit(base1.image, base1.rect)
            screen.blit(base2.image, base2.rect)
            grupo_passarinho.draw(screen)
            score.draw_score(screen, grupo_pipes, screen_rect, grupo_passarinho, my_passarinho)
            score.draw_max_score(screen, screen_rect)
            score.draw_nivel_player(screen, screen_rect)
            vida.check_vida(grupo_pipes, my_passarinho, screen,screen_rect, base1)
            vida.draw_vida(screen)
            update_velocidade_jogo(Pipe, base1, base2)
            if vida.total_vidas <= 0:
                game_activation = False
            vida.check_died(my_passarinho, screen_rect, score, grupo_pipes, Pipe, base1, base2)
            if len(grupo_pipes) == 0:
                pipe.adicionar_pipes(screen_rect, base1, grupo_pipes)

            # calcular milisegundos pra alternar a imagem
            if mover_passaro_cima:
                if (time.time() - tempo_inicio) >= 0.200:
                    my_passarinho.image = imagens_passarinho[0]
                    tempo_inicio = time.time()
                else:
                    my_passarinho.image = imagens_passarinho[2]

            else:
                my_passarinho.image = imagens_passarinho[1]


        clock.tick(30)
        pygame.display.flip()
        


run_game()