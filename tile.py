import pygame
import random

BLANK = 0
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

class Tile:
    def __init__(self) -> None:
        self.entropy = 5
        self.collapsed = False
        self.images = [
            pygame.image.load('Assets/blank.png'),
            pygame.image.load('Assets/up.png'),
            pygame.image.load('Assets/right.png'),
            pygame.image.load('Assets/down.png'),
            pygame.image.load('Assets/left.png')
        ]
        self.image = None
        self.possibles = [0,1,2,3,4]
    
    def get_entropy(self):
        return self.entropy
    
    def ReduceOptions(self, CollapsedCellImage, direction):
        def BlankCollapsed(direction):
            if direction == 'UP':
                NewPossibles = [BLANK,UP]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'RIGHT':
                NewPossibles = [BLANK,RIGHT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'DOWN':
                NewPossibles = [BLANK,DOWN]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'LEFT':
                NewPossibles = [BLANK,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
        def UpCollapsed(direction):
            if direction == 'UP':
                NewPossibles = [RIGHT,DOWN,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'RIGHT':
                NewPossibles = [UP,DOWN,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'DOWN':   
                NewPossibles = [BLANK,DOWN]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'LEFT':
                NewPossibles = [UP,RIGHT,DOWN]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
        def DownCollapsed(direction):
            if direction == 'UP':
                NewPossibles = [BLANK,UP]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'RIGHT':
                NewPossibles = [UP,DOWN,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'DOWN':
                NewPossibles = [UP,RIGHT,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'LEFT':
                NewPossibles = [UP,RIGHT,DOWN]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
        def RightCollapsed(direction):
            if direction == 'UP':
                NewPossibles = [RIGHT,DOWN,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'RIGHT':
                NewPossibles = [UP,DOWN,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'DOWN':
                NewPossibles = [UP,RIGHT,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'LEFT':
                NewPossibles = [BLANK,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
        def LeftCollapsed(direction):
            if direction == 'UP':
                NewPossibles = [RIGHT,DOWN,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'RIGHT':
                NewPossibles = [BLANK,RIGHT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'DOWN':
                NewPossibles = [UP,RIGHT,LEFT]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
            elif direction == 'LEFT':
                NewPossibles = [UP,RIGHT,DOWN]
                intersection = list(set(self.possibles) & set(NewPossibles))
                self.possibles = intersection
        
        if CollapsedCellImage == BLANK:
            BlankCollapsed(direction)
        elif CollapsedCellImage == UP:
            UpCollapsed(direction)
        elif CollapsedCellImage == RIGHT:
            RightCollapsed(direction)
        elif CollapsedCellImage == DOWN:
            DownCollapsed(direction)
        elif CollapsedCellImage == LEFT:
            LeftCollapsed(direction)
            
        self.entropy = len(self.possibles)    
            
    def set_image(self):
        num = random.choice(self.possibles)
        self.image = self.images[num]
        self.possibles = [num]
        self.collapsed = True
        self.entropy = len(self.possibles)
    
    def get_possibles(self):
        return self.possibles
        