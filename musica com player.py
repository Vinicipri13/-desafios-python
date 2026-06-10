import pygame
import sys

# Inicializa o Pygame
pygame.init()
pygame.mixer.init()

# Configurações da janela
largura, altura = 400, 200
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mini Player')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 120, 215)

# Fonte
fonte = pygame.font.SysFont(None, 30)

# Botões
botoes = {
    'play': pygame.Rect(50, 100, 80, 40),
    'pause': pygame.Rect(160, 100, 80, 40),
    'stop': pygame.Rect(270, 100, 80, 40)
}

# Carrega a música
pygame.mixer.music.load('Musica.mp3')


# Função para desenhar os botões
def desenhar_botoes():
    for nome, rect in botoes.items():
        pygame.draw.rect(tela, AZUL, rect)
        texto = fonte.render(nome.capitalize(), True, BRANCO)
        tela.blit(texto, (rect.x + 10, rect.y + 5))


# Loop principal
rodando = True
while rodando:
    tela.fill(PRETO)
    desenhar_botoes()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos
            if botoes['play'].collidepoint(pos):
                pygame.mixer.music.play()
            elif botoes['pause'].collidepoint(pos):
                pygame.mixer.music.pause()
            elif botoes['stop'].collidepoint(pos):
                pygame.mixer.music.stop()

    pygame.display.update()

pygame.quit()
sys.exit()