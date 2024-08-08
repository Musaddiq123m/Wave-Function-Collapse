import pygame
import sys
import random
# from tile import Tile
from tile2 import *
import math

pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400
DIM = 20
screen = pygame.display.set_mode((screen_width, screen_height))

array = [[Tile() for _ in range(DIM)] for _ in range(DIM)]

def RandomMinEntropy(array):
    def MinEntropy(array):
        ans = math.inf
        for i in range(DIM):
            for j in range(DIM):
                if array[i][j].collapsed == False and array[i][j].get_entropy() < ans :
                    ans = array[i][j].get_entropy()
        return ans
    
    min_entropy = MinEntropy(array)
    min_entropy_list = []
    
    for i in range(DIM):
        for j in range(DIM):
            if array[i][j].collapsed == False and array[i][j].get_entropy() == min_entropy :
                min_entropy_list.append((i, j))

    if len(min_entropy_list):                
        return random.choice(min_entropy_list)
    else:
        return (-1, -1)
                        
def dfs(screen, array, start_x, start_y):
    rows, cols = DIM, DIM
    stack = [(start_x, start_y)]
    
    directions = [
        ('UP', -1, 0),    
        ('DOWN', 1, 0),   
        ('LEFT', 0, -1),  
        ('RIGHT', 0, 1)
    ]
    
    while stack:
        temp_x, temp_y = stack.pop()
        
        CollapsedCellImage = array[temp_x][temp_y].possibles[0]
        
        for direction, dx, dy in directions:
            new_x, new_y = temp_x + dx, temp_y + dy
            
            if 0 <= new_x < DIM and 0 <= new_y < DIM and array[new_x][new_y].collapsed == False:
                array[new_x][new_y].reduce_options(CollapsedCellImage, direction)
                if len(array[new_x][new_y].possibles) == 1:
                    array[new_x][new_y].set_image()
                    stack.append((new_x, new_y))
                    draw(screen, array)

    
def draw(screen, array):
    size = screen_width // DIM
    for i in range(DIM):
        for j in range(DIM):
            if array[i][j].get_entropy() == 1:
                screen.blit(pygame.transform.scale(array[i][j].image, (size, size)), (j * size, i * size))

def print_entropy(screen,array):
    for i in range(DIM):
        for j in range(DIM):
            print(array[i][j].get_entropy(), end=' ')    
        print()
    print()
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x, y = RandomMinEntropy(array)
    if x != -1: 
        array[x][y].set_image()
        size = screen_width // DIM
        # screen.blit(pygame.transform.scale(array[x][y].image, (size, size)), (y * size, x * size)) 
        dfs(screen,array, x, y)
        # print_entropy(screen,array)
        
    draw(screen,array)
    pygame.display.flip()
    
    # clock.tick(15)

pygame.quit()
sys.exit()
