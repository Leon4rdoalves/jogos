import pygame

pygame.init()


class Jogo_Corrida:
    def __init__(self):
        self.janela = ''
        self.janela_aberta = True
        self.evento = ''
        self.comandos = ''
        self.x = 400
        self.y = 300
        self.mov = 10

    def iniciar(self):
        try:
            self.janela = pygame.display.set_mode((700, 800))
            pygame.display.set_caption('Ebony ** Corrida')

            while self.janela_aberta:
                pygame.time.delay(50)
                pygame.draw.circle(self.janela, (0, 255, 0), (self.x, self.y), 25)
                pygame.display.update()
                self.janela.fill((0, 0, 0))

                self.comandos = pygame.key.get_pressed()
                if self.comandos[pygame.K_UP]:
                    self.y -= self.mov
                if self.comandos[pygame.K_DOWN]:
                    self.y += self.mov
                if self.comandos[pygame.K_LEFT]:
                    self.x -= self.mov
                if self.comandos[pygame.K_RIGHT]:
                    self.x += self.mov

                for self.evento in pygame.event.get():
                    if self.evento.type == pygame.QUIT:
                        self.janela_aberta = False

            pygame.QUIT()

        except TypeError:
            print('')


comecar = Jogo_Corrida()
comecar.iniciar()
