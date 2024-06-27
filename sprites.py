import pygame

class Char(sprites.Sprite):
    
    def __init__(self):
        sprites.Sprite.__init__(self)
        
        self.spriteSheet = pygame.image.load("resources/sprites/Main/Mario.png").convert_alpha()
        self.image = pygame.transform.scale(self.spriteSheet.subsurface(0,0,200,420),(100,200))
        self.rect = pygame.image.get_rect()
        
    def update():
        pass
    