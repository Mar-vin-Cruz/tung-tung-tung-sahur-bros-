import pygame

class bill:
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load("Grenn_quieto.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def corr(self):
        self.screen.blit(self.image,self.rect)

