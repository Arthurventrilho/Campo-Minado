import pygame as pg 
import sys
from player import Player, Wall, Wall1
from os import path
from tilemap import Map, Camera


WHITE  = (255,255,255)
BLACK = (0,0,0)
RED = (155,0,0)
GREEN = (0,155,0)
BLUE =(0,0,255)
DARKGREY = (40,40,40)
LIGHTGREY = (100,100,100)
YELLOW = (255,255,0)
BRIGHT_GREEN = (0,255,0)
BRIGHT_RED = (255,0,0)
# GAME OPTIONS/SETTINGS
TITLE = "MINE GAME"
WIDTH = 1024
HEIGHT = 768
FPS = 60
BGCOLOR = DARKGREY
TILESIZE =32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#player settings

PLAYER_SPEED = 400
PLAYER_ROT_SPEED = 250.0
PLAYER_IMG = 'mineradorDcopy.png'








class Game(): 
    def __init__(self):
        #initialize game window
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map = Map(path.join(game_folder, 'map.txt'))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
     
    
   
    def new(self):
        #starts a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '.':
                    Wall(self, col, row)
                if tile == 'p':
                    self.player = Player(self, col, row)
                if tile == '2':
                    Wall1(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    
    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000    
            self.events()
            self.update()
            self.draw()
            
    
    def quit(self):
        pg.quit()
        sys.exit()
        
    def update(self):     
          # Game Loop - Update 
        self.all_sprites.update()
        self.camera.update(self.player)
    
    def draw_grid(self):
        for x in range(0,WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x,0), (x, HEIGHT))
        for y in range(0,HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0,y), (WIDTH, y))
    
    
    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()
    
     
    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
   
    
    
    def show_start_screen(self):
       pass
    
    def show_go_screen(self):
        # Game over screen
        pass
    
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

  