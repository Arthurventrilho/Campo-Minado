import pygame
import sys
from pygame.locals import *
import random


# ===============      CLASSES      ===============
class Minerador(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, picaretaDamage, sapatoSpeed, stamina, sono, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damage = picaretaDamage
        self.speed = sapatoSpeed
        self.stamina = stamina
        self.sleep = sono

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        movimento = self.speed
        if pressed_keys[K_LEFT] or (pressed_keys[K_LEFT] and pressed_keys[K_UP]):
            self.image = pygame.image.load("mineradorE.png")
            mover_x = -movimento
            mover_y = 0
        elif pressed_keys[K_RIGHT] or (pressed_keys[K_RIGHT] and pressed_keys[K_UP]):
            self.image = pygame.image.load("mineradorD.png")
            mover_x = +movimento
            mover_y = 0
        elif pressed_keys[K_DOWN]:
            mover_x = 0
            mover_y = +movimento
        elif pressed_keys[K_UP] and pygame.sprite.spritecollide(minerador, escada_group, False):
            mover_x = 0
            mover_y = -movimento  

        else:
            mover_x = 0
            mover_y = 0
        self.rect.x += mover_x
        self.rect.y += mover_y
        
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
        self.stamina -= 1


class Picareta(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, dano, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

    
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damage = dano

class Sapato(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, velocidade, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

    
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = velocidade

class Terra(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, vida, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.life = vida

class Ferro(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, vida, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.life = vida
        
class COBRE(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, vida, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.life = vida        

class OURO(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, vida, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.life = vida        
        
class RUBI(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, vida, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.life = vida        

class DIAMANTE(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, vida, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.life = vida                

class Escada(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y



# ===============      LOOP PRINCIPAL      ===============
comando = 1
while comando != 0:
    
    #Definindo variaveis
    if comando == 1:
        
        fps = 30
        ferro_quant = 0
        
        
        x_display = 200
        display_W = 4 * x_display
        display_H = 3 * x_display
        
        tela = pygame.display.set_mode((display_W, display_H), 0, 32)
        pygame.display.set_caption('MINE GAME')
        
        # Carrega imagem de fundo.
        # (https://wallpapersafari.com/dark-green-background/)
        fundo = pygame.image.load("fundo.jpg").convert()
        
        #Grupo terreno
        terreno_group = pygame.sprite.Group()
        
        # Cria sapato e adiciona em um grupo de Sprites.
        sapato1 = Sapato("mineradorD.png", 10, display_W * 0.25, display_H * 0.75 )
        sapato_group = pygame.sprite.Group()
        sapato_group.add(sapato1)
        
        escada1 = Escada("escada1.png", display_W * 0.5, display_H * 0.25 - 10 )
        escada2 = Escada("escada1.png", display_W * 0.5, display_H * 0.35 - 10 )
        escada3 = Escada("escada1.png", display_W * 0.5, display_H * 0.45 - 10 )
        escada4 = Escada("escada1.png", display_W * 0.5, display_H * 0.55 - 10 )
        escada5 = Escada("escada1.png", display_W * 0.5, display_H * 0.65 - 10)
        escada6 = Escada("escada1.png", display_W * 0.5, display_H * 0.75 - 10 )
        escada_group = pygame.sprite.Group()
        escada_group.add(escada1, escada2, escada3, escada4, escada5, escada6)
        
        # Cria bloco de ferro e adiciona em um grupo de Sprites.
        ferro1 = Ferro("ferro.png", 90, display_W * 0.1, display_H * 0.75 )
        ferro2 = Ferro("ferro.png", 90, display_W * 0.2, display_H * 0.75 )
        ferro3 = Ferro("ferro.png", 90, display_W * 0.3, display_H * 0.75 )
        ferro4 = Ferro("ferro.png", 90, display_W * 0.4, display_H * 0.75 )
        ferro5 = Ferro("ferro.png", 90, display_W * 0.5, display_H * 0.75 )
        ferro6 = Ferro("ferro.png", 90, display_W * 0.6, display_H * 0.75 )
        ferro_group = pygame.sprite.Group()
        ferro_group.add(ferro1, ferro2, ferro3, ferro4, ferro5, ferro6)
        terreno_group.add(ferro1, ferro2, ferro3, ferro4, ferro5, ferro6)
        
        # Cria bloco de terra e adiciona em um grupo de Sprites.
        terra1 = Terra("terra.png", 45, display_W * 0.1, display_H * 0.25 )
        terra2 = Terra("terra.png", 45, display_W * 0.2, display_H * 0.25 )
        terra3 = Terra("terra.png", 45, display_W * 0.3, display_H * 0.25 )
        terra4 = Terra("terra.png", 45, display_W * 0.4, display_H * 0.25 )
        terra5 = Terra("terra.png", 45, display_W * 0.5, display_H * 0.25 )
        terra6 = Terra("terra.png", 45, display_W * 0.6, display_H * 0.25 )
        terra_group = pygame.sprite.Group()
        terra_group.add(terra1, terra2, terra3, terra4, terra5, terra6)
        terreno_group.add(terra1, terra2, terra3, terra4, terra5, terra6)
        
        # Cria picareta e adiciona em um grupo de Sprites.
        picareta1 = Picareta("mineradorD.png", 3, display_W * 0.75, display_H * 0.75 )
        picareta_group = pygame.sprite.Group()
        picareta_group.add(picareta1)
        
        # Cria bloco escada e adiciona em um grupo de Sprites.
        for row in range(ALTURA):
            for column in range(LARGURA):
                DISPLAYSURF.blit(textura[mapa[row][column]], (column*TELA, row*TELA))
        
        # Cria minerador e adiciona em um grupo de Sprites.
        minerador = Minerador("mineradorD.png", picareta1.damage, sapato1.speed, 200, fps*60, display_W * 0.5, display_H * 0.5 )
        minerador_group = pygame.sprite.Group()
        minerador_group.add(minerador)
        
        #RELOGIO   
        relogio = pygame.time.Clock()
        
        #vai para o jogo
        comando = 2
    

    #inicia o jogo    
    if comando == 2:
        
        pygame.init()
        # === NÚMERO DE VEZES QUE O LOOP É REALIZADO POR SEGUNDO ===
        
        tempo = relogio.tick(fps)
    
        # === LIDAR COM EVENTOS ===
    
        # Para cada evento não-processado na lista de eventos:
        for event in pygame.event.get():
            # Verifica se o evento atual é QUIT (janela fechou).
            if event.type == QUIT:
                # para sair do loop de jogo.
                pygame.quit()
                quit()
    

        # === LÓGICA DO JOGO ===
    
        # Move o minerador pela tela.
        minerador.move()
        
        #guardando posicão depois do movimento
        x_player = minerador.rect.x
        y_player = minerador.rect.y
        
        #gravidade 
        if pygame.sprite.spritecollide(minerador, escada_group, False):
            gravidade = 0
        else:
            gravidade = 15
        minerador.rect.y += gravidade
        
        #colisao gravidade (volta para a posicao anterior)
        for terreno in pygame.sprite.spritecollide(minerador, terreno_group, False):
            minerador.rect.y = y_player
        
        #Se o minerador bate nos blocos de ferro
        for ferro in pygame.sprite.spritecollide(minerador, ferro_group, False):
            ferro.life -= minerador.damage
            minerador.colide()
            
            
        for ferro in ferro_group:
            if ferro.life <= 0:
                ferro_quant += 1
                ferro.kill()
        
        #Se o minerador bate nos blocos de terra
        for terra in pygame.sprite.spritecollide(minerador, terra_group, False):
            terra.life -= minerador.damage
            minerador.colide()
    
            
        for terra in terra_group:
            if terra.life <= 0:
                terra.kill()
        
        
        
        
        #O minerador fica mais cansado a cada ciclo        
        minerador.sleep -= 1
        
        
        
        # O minerador morre.
        if minerador.sleep <= 0 or minerador.stamina <= 0:
            comando = 1
        
        
        # === GERA SAÍDAS  ===
    
        # Pinta a imagem de fundo na tela auxiliar.
        tela.blit(fundo, (0, 0))
                      
        # Pinta os elementos do grupo de escadas na tela auxiliar.
        #escada_group.draw(tela)
    
        # Pinta os elementos do grupo dos mineradores na tela auxiliar.
        minerador_group.draw(tela)
        
        # Pinta os elementos do grupo de blocos na tela auxiliar.
        ferro_group.draw(tela)
        terra_group.draw(tela)

    
        # Troca de tela na janela principal.
        pygame.display.update()
   

pygame.quit()
quit()