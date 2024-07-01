import pygame
import sys
#from sprites import Char
from config import *
from menu import *

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