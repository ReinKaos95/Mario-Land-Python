import pygame
from config import *
import os

class Char():
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.spriteSheet = pygame.image.load(SPRITE_PATH + "Main/Mario.png").convert_alpha()
        self.image = pygame.transform.scale(self.spriteSheet.subsurface(0,0,200,420),(100,200))
        self.rect = pygame.image.get_rect()
        
    def update():
        pass
    