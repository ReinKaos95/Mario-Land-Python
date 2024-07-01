import pygame
from config import *

class menu():
    def __init__(self):
        menu = pygame.image.load('resources/sprites/Daisies/TitleScreen.png').convert()
        menu.blit(menu, (RES))