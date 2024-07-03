import pygame
import sys
from config import *
from menu import *
from mario import *
"""
#from sprites import Char


pygame.init()


pygame.display.set_mode(RES)
pygame.display.set_caption(TITLE)
menu = menu()

#mario = Char()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
    
    pygame.display.update()
    """

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.title = pygame.display.set_caption(TITLE)
        
    def newGame(self):
        self.menu = Menu(self)
        self.mario = Mario(self)
        
    def update(self):
        pygame.display.flip()
        
        
    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
        
    def Run(self):
        while True:
            self.events()
            self.update()
            
            
if __name__ == '__main__':
    game = Game()
    game.Run()