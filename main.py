import pygame
import sys
import sprites

pygame.init()


window = pygame.display.set_mode((640,480))

pygame.display.set_caption("Super Mamario Land")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
            
    pygame.display.flip()