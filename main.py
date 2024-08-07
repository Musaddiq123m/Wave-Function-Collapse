import pygame
import sys
import random
from tile import Tile
import math

pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400
DIM = 10
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
                        
def dfs(screen,array, start_x, start_y):
    rows, cols = DIM, DIM
    stack = [(start_x, start_y)]
    while stack:
        temp_x, temp_y = stack.pop()
        
        CollapsedCellImage = array[temp_x][temp_y].possibles[0]
        if temp_x - 1 >= 0 and array[temp_x-1][temp_y].collapsed == False:
            array[temp_x-1][temp_y].ReduceOptions(CollapsedCellImage, 'UP')
            if len(array[temp_x-1][temp_y].possibles) == 1:
                array[temp_x-1][temp_y].set_image()
                stack.append((temp_x-1, temp_y))
                draw(screen,array)
                 
        if temp_x + 1 < DIM and array[temp_x+1][temp_y].collapsed == False:
            array[temp_x+1][temp_y].ReduceOptions(CollapsedCellImage, 'DOWN')
            if len(array[temp_x+1][temp_y].possibles) == 1:
                array[temp_x+1][temp_y].set_image()
                stack.append((temp_x+1, temp_y))
                draw(screen,array)
    
        if temp_y - 1 >= 0 and array[temp_x][temp_y-1].collapsed == False:
            array[temp_x][temp_y-1].ReduceOptions(CollapsedCellImage, 'LEFT')
            if len(array[temp_x][temp_y-1].possibles) == 1:
                array[temp_x][temp_y-1].set_image()
                stack.append((temp_x, temp_y-1))
                draw(screen,array)
                
        if temp_y + 1 < DIM and array[temp_x][temp_y+1].collapsed == False:
            array[temp_x][temp_y + 1].ReduceOptions(CollapsedCellImage, 'RIGHT')
            if len(array[temp_x][temp_y+1].possibles) == 1:
                array[temp_x][temp_y+1].set_image()
                stack.append((temp_x, temp_y+1))
                draw(screen,array)
    
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
