import pygame
from config import *

class Menu():
    def __init__(self):
        self.menu = menu
        self.screen = screen
        self.getMenu()
        
    def getMenu(self):
        menu = pygame.image.load(SPRITE_PATH + 'Daisies/TitleScreen.png')
        screen = RES
        screen.blit(menu)
        
    def filling(self):
        while True:
            for event in pygame.event.get():
                screen.blit(menu)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()

    def update(self):
        self.getMenu()
