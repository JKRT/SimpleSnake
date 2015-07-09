import random
import pygame
class Candy:
    cordinates = [0,0]
    def __init__(self,screen,RED):
        self.cordinates[0] = random.randrange(0,800,5)
        self.cordinates[1] = random.randrange(0,800,5)
        pygame.draw.rect(screen, RED, [self.cordinates[0], self.cordinates[1], 20, 20])
        
