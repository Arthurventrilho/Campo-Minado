import pygame
import random
from pygame.locals import *

class BlocoParams:
    def __init__(self, image, vida):
        self.image = image
        self.life = vida

class Bloco(pygame.sprite.Sprite):
    TERRA = 0
    FERRO = 1
    COBRE = 2
    OURO = 3
    RUBI = 4
    DIAMANTE = 5
    
    tipos = {
        TERRA: BlocoParams(pygame.image.load("terra.png"), 50),
        FERRO: BlocoParams(pygame.image.load("ferro.png"), 100),
        COBRE: BlocoParams(pygame.image.load("diamante.png"), 150),
        OURO: BlocoParams(pygame.image.load("ouro.png"), 200),
        RUBI: BlocoParams(pygame.image.load("ruby.png"), 400),
        DIAMANTE: BlocoParams(pygame.image.load("diamante.png"), 800)
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

TELA = 20
LARGURA = 50
ALTURA = 500

pygame.init()
DISPLAYSURF = pygame.display.set_mode((LARGURA*TELA, ALTURA*TELA))

# Criando os blocos de minerio.
blocos_group = pygame.sprite.Group()

mapa = []
for linha in range(ALTURA):
    blocos_linha = []
    for coluna in range(LARGURA):
        # Criando um novo bloco:
        
        # Escolhe um tipo.
        randomNumber = random.randint(0,50)
        
        if randomNumber == 0:
            tipo = Bloco.DIAMANTE
        elif randomNumber == 1 or randomNumber ==2 or randomNumber ==3:
            tipo = Bloco.RUBI
        elif randomNumber >= 4 and  randomNumber <=6:
            tipo = Bloco.OURO
        elif randomNumber >= 7 and randomNumber <= 10:
            tipo = Bloco.FERRO
        else:
            tipo = Bloco.TERRA

        # Calcula a posição.
        pos_x = coluna*TELA
        pos_y = linha*TELA
        
        # Cria o bloco e adiciona no mapa e no grupo.
        novo_bloco = Bloco(tipo, pos_x, pos_y)
        blocos_linha.append(novo_bloco)
        blocos_group.add(novo_bloco)

    mapa.append(blocos_linha)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            break

    blocos_group.draw(DISPLAYSURF)    
    pygame.display.update()
    
pygame.quit()
