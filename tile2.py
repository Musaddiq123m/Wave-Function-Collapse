import pygame
import random


BLANK = 0
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

BLANKIMAGE = [0,0,0,0]
UPIMAGE    = [1,1,0,1]
RIGHTIMAGE = [1,1,1,0]
DOWNIMAGE  = [0,1,1,1]
LEFTIMAGE  = [1,0,1,1]

opposites = {
    'UP'    : 'DOWN',
    'DOWN'  : 'UP',
    'RIGHT' : 'LEFT',
    'LEFT'  : 'RIGHT'
}

patterns = [
    BLANKIMAGE,  
    UPIMAGE,     
    RIGHTIMAGE,  
    DOWNIMAGE,   
    LEFTIMAGE    
]
    
direction_map = {
    'UP': 0,
    'RIGHT': 1,
    'DOWN': 2,
    'LEFT': 3
}

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
        self.possibles = []
        for i in range(self.entropy):
            self.possibles.append(i)
    
    def get_entropy(self):
        return self.entropy
    
    def reduce_options(self, CollapsedCellImage, direction):
        
        CollapsedCellpattern = patterns[CollapsedCellImage]

        OppositeDirection = opposites[direction]
        
        ImageCheckingIndex = direction_map[direction] # bhai agar Up tile collapse hoa he and me uske right pe ho to
        #i need to check if up ka right yani 2nd index is equal to this right wala ka left index
        OppositeCheckingIndex = direction_map[OppositeDirection]
        
        NewPossibles = []
        for possible in self.possibles:
            PossiblePattern = patterns[possible]
            if CollapsedCellpattern[ImageCheckingIndex] == PossiblePattern[OppositeCheckingIndex]:
                NewPossibles.append(possible)
        
        self.possibles = NewPossibles
        self.entropy= len(self.possibles)
        
        
        
         
    def set_image(self):
        num = random.choice(self.possibles)
        self.image = self.images[num]
        self.possibles = [num]
        self.collapsed = True
        self.entropy = len(self.possibles)
    
    def get_possibles(self):
        return self.possibles
        