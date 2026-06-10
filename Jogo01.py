import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Tela
largura, altura = 800, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Bulldog Runner - Pulo Variável')

# Clock
clock = pygame.time.Clock()
FPS = 60

# Carrega imagem do bulldog
bulldog_img = pygame.image.load('ChatGPT Image 27 de fev. de 2026, 22_21_50.png')
bulldog_img = pygame.transform.scale(bulldog_img, (80, 80))
bulldog_largura, bulldog_altura = bulldog_img.get_size()

# Posição inicial do bulldog
bulldog_x = 100
bulldog_y = altura - bulldog_altura - 30
bulldog_vel_y = 0
gravidade = 1
no_chao = True

# Pulo variável
pulo_vel = -15  # impulso inicial do pulo
pulo_max = -25  # limite máximo do pulo se segurar
pulo_atual = 0
pulando = False

# Obstáculos
obs_largura, obs_altura = 30, 50
obstaculos = []
obs_vel = 10

# Pontuação
pontos = 0
fonte = pygame.font.SysFont(None, 35)


# Função para desenhar tudo
def desenhar():
    tela.fill((200, 200, 200))  # fundo cinza
    tela.blit(bulldog_img, (bulldog_x, bulldog_y))
    for obs in obstaculos:
        pygame.draw.rect(tela, (0, 0, 0), obs)
    texto = fonte.render(f'Pontos: {pontos}', True, (0, 0, 0))
    tela.blit(texto, (10, 10))
    pygame.display.update()


# Loop principal
rodando = True
while rodando:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        # Começa o pulo
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and no_chao:
                pulando = True
                bulldog_vel_y = pulo_vel
                no_chao = False
        # Para de segurar a barra
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE:
                pulando = False

    # Aplica gravidade
    bulldog_vel_y += gravidade

    # Enquanto segurando barra de espaço, aumenta impulso (pulo mais alto)
    if pulando and bulldog_vel_y > pulo_max:
        bulldog_vel_y -= 0.5  # ajuste a força do pulo
        if bulldog_vel_y < pulo_max:
            bulldog_vel_y = pulo_max

    bulldog_y += bulldog_vel_y

    # Checa se voltou ao chão
    if bulldog_y >= altura - bulldog_altura - 30:
        bulldog_y = altura - bulldog_altura - 30
        bulldog_vel_y = 0
        no_chao = True

    # Criar obstáculos aleatórios
    if random.randint(1, 50) == 1:
        obs_x = largura
        obs_y = altura - obs_altura - 30
        obstaculos.append(pygame.Rect(obs_x, obs_y, obs_largura, obs_altura))

    # Movimenta obstáculos
    for obs in obstaculos:
        obs.x -= obs_vel
        if obs.colliderect(pygame.Rect(bulldog_x, bulldog_y, bulldog_largura, bulldog_altura)):
            print(f'Game Over! Sua pontuação: {pontos}')
            rodando = False
        if obs.x + obs_largura < 0:
            obstaculos.remove(obs)
            pontos += 1

    desenhar()

pygame.quit()
sys.exit()