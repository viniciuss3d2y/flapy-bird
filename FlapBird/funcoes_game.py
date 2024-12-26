import time

tempo_comeco = time.time()

def update_velocidade_jogo(pipe, base1, base2):
    global tempo_comeco
    tempo_agora = time.time()
    if tempo_agora - tempo_comeco >= 8:
        base1.velovidade_base += 0.3
        base2.velovidade_base += 0.3
        pipe.velocidade_pipe += 0.3
        tempo_comeco = tempo_agora