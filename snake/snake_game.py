import pygame
from pygame.locals import *
from random import randint


def colisão(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def grid():
    x = randint(0, 59)
    y = randint(0, 59)
    return x * 10, y * 10


def Jogo():
    cima = 0
    direita = 1
    baixo = 2
    esquerda = 3

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Ebony * Snake')

    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10, 10))

    maçã = pygame.Surface((10, 10))
    maçã.fill((255, 0, 0))  # Vermelho
    maçã_pos = grid()

    direção = esquerda

    velocidade = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont('Ubuntu', 18)
    pontos = 0

    gameover = False

    while not gameover:
        if pontos < 10:
            velocidade.tick(10)
            snake_skin.fill((205, 205, 205))
        elif pontos < 20:
            velocidade.tick(12)
            snake_skin.fill((0, 127, 225))
        elif pontos < 40:
            velocidade.tick(14)
            snake_skin.fill((235, 199, 158))
        elif pontos < 60:
            velocidade.tick(18)
            snake_skin.fill((255, 0, 255))
        elif pontos < 100:
            velocidade.tick(20)
            snake_skin.fill((127, 0, 255))
        elif pontos < 150:
            velocidade.tick(25)
            snake_skin.fill((255, 165, 0))
        elif pontos < 200:
            velocidade.tick(30)
            snake_skin.fill((255, 255, 0))
        elif pontos < 250:
            velocidade.tick(35)
            snake_skin.fill((140, 23, 23))

        else:
            velocidade.tick(40)
            snake_skin.fill((255, 0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

            if evento.type == KEYDOWN:
                if evento.key == K_UP and direção != baixo:
                    direção = cima
                if evento.key == K_DOWN and direção != cima:
                    direção = baixo
                if evento.key == K_LEFT and direção != direita:
                    direção = esquerda
                if evento.key == K_RIGHT and direção != esquerda:
                    direção = direita

        if colisão(snake[0], maçã_pos):
            maçã_pos = grid()
            snake.append((0, 0))
            pontos += 1

        # Verificando se a snake acerta as laterais.
        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
            gameover = True
            break

        # Verificando se a snake acerta a si mesma.
        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                gameover = True
                break

        if gameover:
            break

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        # Movimentação incrementada
        if direção == cima:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if direção == baixo:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if direção == direita:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if direção == esquerda:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        screen.fill((0, 0, 0))
        screen.blit(maçã, maçã_pos)

        # Desenho das linhas
        for x in range(0, 600, 10):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
        for y in range(0, 600, 10):
            pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

        pontos_font = font.render('Pontos: %s' % pontos, True, (255, 255, 255))
        pontos_rect = pontos_font.get_rect()
        pontos_rect.topleft = (600 - 120, 10)
        screen.blit(pontos_font, pontos_rect)

        for posição in snake:
            screen.blit(snake_skin, posição)

        pygame.display.update()

    while True:
        gameover_font = pygame.font.Font(None, 90)
        gameover_screen = gameover_font.render('Game Over!', True, (0, 220, 0))
        gameover_rect = gameover_screen.get_rect()
        gameover_rect.midtop = (500 / 2, 10)
        screen.blit(gameover_screen, gameover_rect)
        name_font = pygame.font.Font(None, 30)
        name_screen = name_font.render('@ebony.prog', True, (0, 255, 200))
        name_rect = name_screen.get_rect()
        name_rect.midtop = (500 / 3.5, 65)
        screen.blit(name_screen, name_rect)

        pygame.display.update()
        pygame.time.wait(500)

        while True:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
