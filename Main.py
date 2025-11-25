import pygame
import sys

class Tung_Tung_Sahur_Team:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960,540))
        pygame.display.set_caption("Tung Tung Sahur Team")

    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

if __name__ == "__main__":
    a = Tung_Tung_Sahur_Team()
    a.corre_juego()