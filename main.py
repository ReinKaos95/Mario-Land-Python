import pygame
import sys
from sprites import Char

pygame.init()


window = pygame.display.set_mode((640,480))

pygame.display.set_caption("Super Mamario Land")

mario = Char()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
            
    pygame.display.flip()