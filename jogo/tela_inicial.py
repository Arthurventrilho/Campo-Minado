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

# player settings
PLAYER_SPEED = 400
PALYER_IMG = 'mineradorDcopy.png'
PLAYER_ROT_SPEED = 250.0
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0
    
    def get_keys(self):
        self.rot.speed = 0 
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.eot_speed = -PLAYER_ROT_SPEED
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)        
        
    def collide_with_walls(self, dire):
        if dire == 'x':
            hits = pg.sprite.spritecollide(self,self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0 
                self.rect.x = self.pos.x
        if dire == 'y':
            hits = pg.sprite.spritecollide(self,self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0 
                self.rect.y = self.pos.y    
            
    
    
    def update(self):
        self.get_keys()
        self.rrot = (self.rot + self.rot_speed + self.game.dt) % 360
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos. y
        self.collide_with_walls('y')
        
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE,  TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y  
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE