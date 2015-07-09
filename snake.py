import copy
import pygame
import numpy

class Direction:
    left = 0
    right = 1
    up = 2
    down = 3
    current_direction = 1

    def __init__(self):
        self.left = 0
        self.right = 1
        self.up = 2
        self.down = 3 
        
class Snake:

    head = [0,0] # [0] for x-cordiantes , [1] for y cordinate, represents where the head is
    tail = []
    end = [] #End of the snake
    size = 0 # Size of snake is initialized to one
    direction = Direction()
    
    def __init__(self):
        self.head = [0,0]
        self.size = 1
        direction = Direction()
        self.end = self.head
    def set_direction(self,dirc):
        self.direction.current_direction = dirc 
        
    def get_current_direction(self):
        return self.direction.current_direction
   
    def get_cordinates(self):
        return self.head
        
    def place_snake(self):
        x = head[0]
        y = head[1]
        prev = [0.0]
        for i in range(0,len(tail)):
            if i != 0:
                prev[0] = tail[i-1].cordinates[0]
                prev[1] = tail[i-1].cordinates[1]
            elif i == 0:
                prev[0] = self.head[0]
                prev[1] = self.head[1]

            part.cordinate[0] = prev[0]
            part.cordinate[1] = prev[1]
            
    def draw_snake(self,BLUE,screen):
       self.draw_head(BLUE,screen)
       for cord in self.tail:
           pygame.draw.rect(screen,BLUE,[cord[0],cord[1],20,20])

    def update_tail(self,prev): #prev is the heads previous posistion
        if len(self.tail) > 0:
           self.tail.insert(0,prev)
           self.end = copy.deepcopy(self.tail.pop()) #Trailing behind..
        else:
            self.end = self.head

    def draw_head(self,BLUE,screen):
        pygame.draw.rect(screen, BLUE, [self.head[0], self.head[1], 20, 20])

    def eats(self,BLACK,screen,apple_cordinates):
        pygame.draw.rect(screen,BLACK,[apple_cordinates[0],apple_cordinates[1] ,20,20])
        self.size += 1
        cords = copy.deepcopy(self.head) # 
        self.tail.append(cords)
