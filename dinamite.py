import pygame
import random
from pygame.locals import *




# ===============      CLASSES      =============== 
class Mapa():   
    def __init__(self, tamanhoBloco, altura, largura):
        self.tbloco = tamanhoBloco
        self.largura = largura
        self.altura = altura
        self.alturat = tamanhoBloco * altura
        self.largurat = tamanhoBloco * largura

        
    def criando(self):
        all_sprites.add(minerador)
        blocos = pygame.sprite.Group()
        for linha in range(self.altura):
        
            for coluna in range(self.largura):
                tipo = - 1
                if linha <= 2:
                    tipo = -1
                elif linha == 3 or linha == (self.altura-1):
                    tipo = Bloco.GRANITO
                elif coluna == 0 or coluna == (self.largura-1):
                    tipo = Bloco.GRANITO
                elif coluna == 1 and linha == posJogador:
                    tipo = -1
                elif coluna == mapa.largura-2 and linha == posBandeira:
                    tipo = Bloco.BANDEIRA
                else:
                    chance = random.randrange(0, 1000)
                    if chance >= 0 and chance <=499:
                        tipo = Bloco.TERRA
                    elif chance >= 500 and chance <=849:
                        tipo = Bloco.DINAMITE_VISIVEL
                    elif chance >= 850 and chance <=959:
                        tipo = Bloco.GRANITO
                    elif chance >= 960 and chance <=989:
                        tipo = Bloco.VIDA
                    else:
                        tipo = Bloco.DINAMITE_INVISIVEL
        
                if tipo != -1:    
                    # Calcula a posição.
                    pos_x = coluna * self.tbloco
                    pos_y = linha * self.tbloco
                    
                    # Cria o bloco e adiciona no mapa e no grupo.
                    novo_bloco = Bloco(tipo, pos_x, pos_y)
                    all_sprites.add(novo_bloco)
                    blocos.add(novo_bloco)
                    
        self.all =  all_sprites
        self.blocos = blocos

class MineradorImagem():
    def __init__(self, image1, image2):
        self.image1 = pygame.image.load(image1)
        self.image2 = pygame.image.load(image2)
    

class Minerador(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, picaretaDamage, sapatoSpeed, vida, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = arquivo_imagem
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damage = picaretaDamage
        self.speed = sapatoSpeed
        self.life = vida
        self.lastrect = Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.image = mineradorImagem.image2
            self.velocidadex = -self.speed
            self.velocidadey = 0
        elif pressed_keys[K_RIGHT]:
            self.image = mineradorImagem.image1
            self.velocidadex = +self.speed
            self.velocidadey = 0
        elif pressed_keys[K_DOWN]:
            self.velocidadex = 0
            self.velocidadey = +self.speed
        elif pressed_keys[K_UP]:
            self.velocidadex = 0
            self.velocidadey = -self.speed 

        else:
            self.velocidadex = 0
            self.velocidadey = 0
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        
    def colisao_blocos(self, listaSprites):
    
    
        #Se o minerador bate nos blocos 
        for bloco in pygame.sprite.spritecollide(self, listaSprites, False):
            if bloco.tipo != 4:    
                bloco.life -= minerador.damage
            
            minerador.colide()
            if bloco.life <=0:
                bloco.kill()
                if bloco.tipo == 1 or bloco.tipo == 2:  
                    minerador.life -= 1
                if bloco.tipo == 5:  
                    minerador.life += 1
                if bloco.tipo == 3:  
                    minerador.life += 100

        
    def colide(self):
        pressed_keys = pygame.key.get_pressed()
        movimento = self.speed + 1
        if pressed_keys[K_LEFT]:
            mover_x = -movimento
            mover_y = 0
        elif pressed_keys[K_RIGHT]:
            mover_x = +movimento
            mover_y = 0
        elif pressed_keys[K_UP]:
            mover_x = 0
            mover_y = -movimento  
        elif pressed_keys[K_DOWN]:
            mover_x = 0
            mover_y = +movimento
        else:
            mover_x = 0
            mover_y = 0
        self.rect.x -= mover_x
        self.rect.y -= mover_y





class BlocoParams:
    def __init__(self, image, vida):
        self.image = image
        self.life = vida

class Bloco(pygame.sprite.Sprite):
    TERRA = 0
    DINAMITE_VISIVEL = 1
    DINAMITE_INVISIVEL = 2
    BANDEIRA = 3
    GRANITO = 4
    VIDA =5

    
    tipos = {
        TERRA: BlocoParams(pygame.image.load("terra.png"), 30),
        DINAMITE_VISIVEL: BlocoParams(pygame.image.load("ferro.png"), 1),
        DINAMITE_INVISIVEL: BlocoParams(pygame.image.load("terra.png"), 1),
        BANDEIRA: BlocoParams(pygame.image.load("escada1.png"), 1),
        GRANITO: BlocoParams(pygame.image.load("diamante.png"), 1),
        VIDA: BlocoParams(pygame.image.load("ruby.png"), 1)

    }
        
    def __init__(self, tipo, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.tipo = tipo
        self.image = Bloco.tipos[tipo].image
        self.life = Bloco.tipos[tipo].life
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

BLACK =  (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



#RELOGIO   
relogio = pygame.time.Clock()

numeroEscadas = 10

pygame.init()

mapa = Mapa(40, 17, 30)
all_sprites = pygame.sprite.Group()

tempo = relogio.tick(30)

DISPLAYSURF = pygame.display.set_mode((mapa.largurat, mapa.alturat))

fundo = pygame.image.load("fundo.jpg").convert()








posJogador = random.randrange(4, mapa.altura-2)
posBandeira = random.randrange(4, mapa.altura-2)
# Cria minerador e adiciona em um grupo de Sprites.
mineradorImagem = MineradorImagem("mineradorD.png", "mineradorE.png")
minerador = Minerador(mineradorImagem.image1 , 1, 1, 10, 1 * 40, posJogador * 40 )
minerador_group = pygame.sprite.Group()
minerador_group.add(minerador)




# Criando os blocos de minerio.

mapa.criando()




#for linha in range(ALTURA):
#
#    for coluna in range(LARGURA):
#        tipo = - 1
#        if linha <= 2:
#            tipo = -1
#        elif linha == 3 or linha == (ALTURA-1):
#            tipo = Bloco.GRANITO
#        elif coluna == 0 or coluna == (LARGURA-1):
#            tipo = Bloco.GRANITO
#        elif coluna == 1 and linha == posJogador:
#            tipo = -1
#        elif coluna == LARGURA-2 and linha == posBandeira:
#            tipo = Bloco.BANDEIRA
#        else:
#            chance = random.randrange(0, 1000)
#            if chance >= 0 and chance <=499:
#                tipo = Bloco.TERRA
#            elif chance >= 500 and chance <=849:
#                tipo = Bloco.DINAMITE_VISIVEL
#            elif chance >= 850 and chance <=959:
#                tipo = Bloco.GRANITO
#            elif chance >= 960 and chance <=989:
#                tipo = Bloco.VIDA
#            else:
#                tipo = Bloco.DINAMITE_INVISIVEL
#
#        if tipo != -1:    
#            # Calcula a posição.
#            pos_x = coluna*TELA
#            pos_y = linha*TELA
#            
#            # Cria o bloco e adiciona no mapa e no grupo.
#            novo_bloco = Bloco(tipo, pos_x, pos_y)
#            all_sprites.add(novo_bloco)
#            blocos.add(novo_bloco)
    


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        
    if minerador.life <= 0:
        pygame.quit()
        quit()
            

            
    # Move o minerador pela tela.
    minerador.move()

    minerador.colisao_blocos(mapa.blocos)

    DISPLAYSURF.blit(fundo, (0, 3 * 40))    

    mapa.all.draw(DISPLAYSURF) 
    
    print(minerador.life)
    pygame.display.update()