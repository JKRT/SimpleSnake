#************************
# Author: John Tinnerholm
#************************
# To do add highscores and a start menu
# Fix candy bug and framerate problem

import pygame
import snake
import candy
import os,sys
import time
import copy
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

size = [1000,1000]
screen=pygame.display.set_mode(size);
pygame.display.set_caption("Snake!")
snake_head_rect = pygame.Rect([75, 10, 25, 20]) 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

def paus_mode():
    while True:
        event = pygame.event.wait()
        key = pygame.key.get_pressed()          
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if key[pygame.K_p]:
                return
    
def keyboard_event(Snake,Direction,out_of_range):
    for event in pygame.event.get():
	if event.type is QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()   
            if key[pygame.K_LEFT] and Snake.get_current_direction() != Direction.right: 
                Snake.set_direction(Direction.left)
                break
            if key[pygame.K_RIGHT] and Snake.get_current_direction() != Direction.left:
                    Snake.set_direction(Direction.right)
                    break
            if key[pygame.K_UP] and Snake.get_current_direction() != Direction.down: 
                Snake.set_direction(Direction.up)
                break
            if key[pygame.K_DOWN] and Snake.get_current_direction() != Direction.up: 
                Snake.set_direction(Direction.down)
                break
            if key[pygame.K_p]:
                paus_mode()
                break

def move_snake(Snake,Direction,out_of_range):
    prev = copy.deepcopy(Snake.head)
    
    if Snake.head[0] >= 1000:
            Snake.head[0] = 1
    elif Snake.head[0] <= 0:
            Snake.head[0] = 1001 
    elif Snake.head[1] <= 0:
            Snake.head[1] = 1001
    elif Snake.head[1] >= 1000:
            Snake.head[1] = 1
    if Snake.direction.current_direction == Direction.left:
            Snake.head[0] -= 20
    if Snake.direction.current_direction == Direction.right:
            Snake.head[0] += 20        
    if Snake.direction.current_direction == Direction.up:
            Snake.head[1] -= 20
    if Snake.direction.current_direction == Direction.down:
            Snake.head[1] += 20
    
    Snake.update_tail(prev)

def coli(head,Snake):
  if len(Snake.tail) == 0 or len(Snake.tail) ==1: #Special case 
      return False
  if len(Snake.tail) > 1 and  Snake.tail[-1] == head:
    return False
  elif head not in Snake.tail:
      return False
  else:
    return True

def end_of_game():
    while True:
        event = pygame.event.wait()
        key = pygame.key.get_pressed()          
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 

def main():
    Snake = snake.Snake()
    Direction = snake.Direction()
    placed = False; apple_cordinates = [0 , 0]
    score = 0; speed = 0;factor = 0 #factor increases for every bite
    out_of_range = False
 
    while True:
        clock.tick(10+speed)
        if coli(Snake.head,Snake):
            myfont = pygame.font.SysFont("monospace", 70)
            label = myfont.render("Score " + str(score), 1, (200,200,0))
            screen.blit(label, (300, 200))
            label = myfont.render("GAME OVER", 1, (255,255,0))
            screen.blit(label, (300, 300))
            end_of_game()

        if not placed: # Check if the apple is placed 
            apple = candy.Candy(screen,RED)
            apple_cordinates = apple.cordinates
            placed = True
      
        keyboard_event(Snake,Direction,out_of_range)
        pygame.draw.rect(screen,BLACK,[Snake.end[0],Snake.end[1],20,20])        
        move_snake(Snake,Direction,out_of_range)
        Snake.draw_snake(BLUE,screen)   

        if Snake.head[0] in range(apple_cordinates[0]-20,apple_cordinates[0]+20) and Snake.head[1] in range(apple_cordinates[1]-20,apple_cordinates[1] + 20):
            score += 1
            score += factor
            factor += 1
            placed = False
            speed += 1
            Snake.eats(BLACK,screen,apple_cordinates)
        pygame.display.flip()
if __name__ == "__main__":
    main()            
