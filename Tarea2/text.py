import pygame

class Text:
    def __init__(self, FontName=None, FontSize=100):
        pygame.font.init()
        self.font = pygame.font.Font(FontName, FontSize)
        self.size = FontSize

    def render(self, surface, text, color, pos):
        x, y = pos
        for i in text.split("\r"):
            surface.blit(self.font.render(i, 1, color), (x, y))
            y += self.size
    def texto(self,puntaje,bestpuntaje):
        pygame.init()
        white = (255, 255, 255)
        size = width, height = 1200, 600
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Flappy Dunk Chanta")
        color = (255, 0, 0)
        text = Text()
        seguir=True
        fuente = pygame.font.Font(None, 200)
        gameover = fuente.render("GAME OVER",True, (0,0,0))
        fuente2 = pygame.font.Font(None, 50)
        continuar = fuente2.render("Para reintentar presione C y para salir presione Q", True, (0,0,0))
        fuente3=pygame.font.Font(None,50)
        mejor=fuente3.render("Mejor puntaje: "+str(bestpuntaje),True,(0,0,0))
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        seguir=False
            screen.fill(color)
            screen.blit(gameover, [200, 50])
            screen.blit(continuar, [200, 500])
            screen.blit(mejor,[450,350])
            text.render(screen,'Puntuación: '+str(puntaje), white, (350, 250))
            pygame.display.flip()



