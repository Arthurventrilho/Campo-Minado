import pygame
import sys
import random
from pygame.locals import *

BLACK =  (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

TERRA = 0
FERRO = 1
COBRE = 2
OURO = 3
RUBI = 4
DIAMANTE = 5


textura = {
        TERRA : pygame.image.load("terra.png"),
        FERRO : pygame.image.load("ferro.png"),
        COBRE : pygame.image.load("diamante.png"),
        OURO : pygame.image.load("ouro.png"),
        RUBI : pygame.image.load("ruby.png"),
        DIAMANTE : pygame.image.load("diamante.png")
        }


        
TELA = 20
LARGURA = 30
ALTURA = 20

resources = [TERRA, FERRO, COBRE, OURO, RUBI, DIAMANTE]
mapa = [ [TERRA for w in range(LARGURA)] for h in range(ALTURA)]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((LARGURA*TELA, ALTURA*TELA))

for rw in range(ALTURA):
    for cl in range(LARGURA):
        randomNumber = random.randint(0,50)
        
        if randomNumber == 0:
            tipo = DIAMANTE
        elif randomNumber == 1 or randomNumber ==2 or randomNumber ==3:
            tipo = RUBI
        elif randomNumber >= 4 or randomNumber <=12:
            tipo = OURO
        elif randomNumber >= 13 or randomNumber <= 28:
            tipo = FERRO
        else:
            tipo = TERRA
        mapa[rw][cl] = tipo

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    for row in range(ALTURA):
        for column in range(LARGURA):
           DISPLAYSURF.blit(textura[mapa[row][column]], column*TELA, row*TELA)
            
    pygame.display.update()
    
    


















