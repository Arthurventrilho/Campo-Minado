import pygame as pg

# DEFINING COLORS 
WHITE  = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE =(0,0,255)
DARKGREY = (40,40,40)
LIGHTGRAY = (100,100,100)
YELLOW = (255,255,0)

# GAME OPTIONS/SETTINGS
TITLE = "MINE GAME"
WIDTH = 1024
HEIGHT = 768
FPS = 60
BGCOLOR = DARKGREY
TILESIZE =32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE







class Map():   
    def __init__(self, filename):
        self.data = []
        with open (filename, 'r') as f:
            for line in f:
                self.data.append(line.strip())
    
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
        
        
class Camera():
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
        
    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2) 
        y = -target.rect.y + int(HEIGHT / 2)
        
        
        
        #limit scrolling to map size
        x = min(0,x) #left
        y = min(0,y) #top
        x = max(-(self.width - WIDTH), x) #right
        y = max(-(self.height - HEIGHT), y) #bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
        
        
        
        