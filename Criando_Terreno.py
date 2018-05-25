import pygame
import random
from pygame.locals import *

"""Retirado de https://github.com/mchr3k/bounce-game/blob/master/bounce.py"""               
def collide(bloco, player): 
    if (bloco.rect.colliderect(player.rect)):
        if ((player.velocidadex == 0) or
            ((player.velocidadex > 0) and
              (bloco.rect.left < player.lastrect.right)) or
            ((player.velocidadex < 0) and
              (player.lastrect.left < bloco.rect.right))):
            # Player was previously above/below the platform
            if (player.velocidadey > 0):
                # Player is falling
                player.rect.bottom = bloco.rect.top
                player.onground = True

            else:
                # Player is rising
                player.rect.top = bloco.rect.bottom
            player.velocidadey = 0
        else:
            # Player has hit an edge
            if (player.velocidadex > 0):
                # Player is moving right
                player.rect.right = bloco.rect.left
            else:
                # Player is moving left
                player.rect.left = bloco.rect.right
            player.velocidadex = 0


def Colisao_Blocos(mapa):
    

    mapas = [mapa[linhaJogador-1][0], mapa[linhaJogador][0], mapa[linhaJogador+1][0]]
    
    for m in mapas:
        #Se o minerador bate nos blocos 
        for bloco in pygame.sprite.spritecollide(minerador, m, False):
            collide(bloco, minerador)

            bloco.life -= minerador.damage
            minerador.colide()
            if bloco.life <=0:
                bloco.kill()

            

def FazendoEscadas(numeroEscadas): 
    numero = 0           
    contadorEscadas = 0          
    for escada in mapa[linhaJogador][1]:
        if colunaJogador != escada.rect.x // TELA:
            contadorEscadas += 0
        else:
            contadorEscadas += 1
            

            
    pressed_keys = pygame.key.get_pressed()
    if contadorEscadas == 0 and pressed_keys[K_UP] and linhaJogador > 5 and numeroEscadas > 0:
        tipo = Bloco.ESCADA
        # Calcula a posição.
        pos_x = colunaJogador *TELA
        pos_y = linhaJogador * TELA
        # Cria o bloco e adiciona no mapa e no grupo.
        novo_bloco = Bloco(tipo, pos_x, pos_y)
        mapa[linhaJogador][1].add(novo_bloco)
        escadas_group.add(novo_bloco)
        numero = 1
    return numero
        
            
            
def Escadas_de_Volta():
    contador = 0
    pressed_keys = pygame.key.get_pressed()
    #Se o minerador bate nos blocos 
    for escada in pygame.sprite.spritecollide(minerador, mapa[linhaJogador-1][1], False):
        if pressed_keys[K_e]:
            escada.kill()
            contador += 1
    #Se o minerador bate nos blocos 
    for escada in pygame.sprite.spritecollide(minerador, mapa[linhaJogador][1], False):
        if pressed_keys[K_e]:
            escada.kill()
            contador += 1
    #Se o minerador bate nos blocos 
    for escada in pygame.sprite.spritecollide(minerador, mapa[linhaJogador+1][1], False):
        if pressed_keys[K_e]:
            escada.kill()
            contador += 1
            
    return contador
# ===============      CLASSES      ===============
class Inventario():
    def __init__(self, tamanho, numeroFerro, numeroCobre, numeroOuro, numeroRubi, numeroDiamante, numeroEscadas):
        self.tamanho = tamanho
        self.ferro = numeroFerro
        self.cobre = numeroCobre
        self.ouro = numeroOuro
        self.rubi = numeroRubi
        self.diamante = numeroDiamante
        self.inventario = self.ferro + self.cobre + self.ouro + self.rubi + self.diamante
        self.escadas = numeroEscadas
        
    def adiciona(self, tipo):
        if self.inventario < self.tamanho:
            if tipo == Bloco.FERRO:
                self.ferro += 1
            elif tipo == Bloco.COBRE:
                self.cobre += 1
            elif tipo == Bloco.OURO:
                self.ouro += 1
            elif tipo == Bloco.RUBI:
                self.rubi += 1
            elif tipo == Bloco.DIAMANTE:
                self.diamante += 1
                
        self.inventario = self.ferro + self.cobre + self.ouro + self.rubi + self.diamante    

class MineradorImagem():
    def __init__(self, image1, image2):
        self.image1 = pygame.image.load(image1)
        self.image2 = pygame.image.load(image2)
    

class Minerador(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, picaretaDamage, sapatoSpeed, stamina, sono, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = arquivo_imagem
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damage = picaretaDamage
        self.speed = sapatoSpeed
        self.stamina = stamina
        self.sleep = sono
        self.lastrect = Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or (pressed_keys[K_LEFT] and pressed_keys[K_UP]):
            self.image = mineradorImagem.image2
            self.velocidadex = -self.speed
            self.velocidadey = 0
        elif pressed_keys[K_RIGHT] or (pressed_keys[K_RIGHT] and pressed_keys[K_UP]):
            self.image = mineradorImagem.image1
            self.velocidadex = +self.speed
            self.velocidadey = 0
        elif pressed_keys[K_DOWN]:
            self.velocidadex = 0
            self.velocidadey = +self.speed
        elif pressed_keys[K_UP] and pygame.sprite.spritecollide(minerador, mapa[linhaJogador - 1][1], False)\
            or pressed_keys[K_UP] and pygame.sprite.spritecollide(minerador, mapa[linhaJogador][1], False)\
            or pressed_keys[K_UP] and pygame.sprite.spritecollide(minerador, mapa[linhaJogador + 1][1], False):
            self.velocidadex = 0
            self.velocidadey = -self.speed 

        else:
            self.velocidadex = 0
            self.velocidadey = 0
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        
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
    ESCADA = 6
    
    tipos = {
        TERRA: BlocoParams(pygame.image.load("terra.png"), 50),
        FERRO: BlocoParams(pygame.image.load("ferro.png"), 100),
        COBRE: BlocoParams(pygame.image.load("cobre.png"), 150),
        OURO: BlocoParams(pygame.image.load("ouro.png"), 200),
        RUBI: BlocoParams(pygame.image.load("ruby.png"), 400),
        DIAMANTE: BlocoParams(pygame.image.load("diamante.png"), 800),
        ESCADA: BlocoParams(pygame.image.load("escada1.png"), 800)
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

TELA = 40
LARGURA = 31
ALTURA = 15

#RELOGIO   
relogio = pygame.time.Clock()

numeroEscadas = 10

pygame.init()



tempo = relogio.tick(30)

DISPLAYSURF = pygame.display.set_mode((LARGURA*TELA, ALTURA*TELA))

fundo = pygame.image.load("fundo.jpg").convert()



# Cria sapato e adiciona em um grupo de Sprites.
sapato1 = Sapato("mineradorD.png", 3, 40, 40 )
sapato_group = pygame.sprite.Group()
sapato_group.add(sapato1)


# Cria picareta e adiciona em um grupo de Sprites.
picareta1 = Picareta("mineradorD.png", 1, 40, 40 )
picareta_group = pygame.sprite.Group()
picareta_group.add(picareta1)


# Cria minerador e adiciona em um grupo de Sprites.
mineradorImagem = MineradorImagem("mineradorD.png", "mineradorE.png")
minerador = Minerador(mineradorImagem.image1 , picareta1.damage, sapato1.speed, 200, 30*60, 15 * 40, (5 * 40) + 10 )
minerador_group = pygame.sprite.Group()
minerador_group.add(minerador)

# Criando os blocos de minerio.
blocos_group = pygame.sprite.Group()
escadas_group = pygame.sprite.Group()

mapa = []
for linha in range(ALTURA):
    blocos_linha = pygame.sprite.Group()
    escadas_linha = pygame.sprite.Group()
    linha_sprites = []
    if linha > 5 and linha <= 10:
        for coluna in range(LARGURA):
            if coluna == int(LARGURA / 2):
                tipo = Bloco.ESCADA
            else:
                # Criando um novo bloco:
                
                # Escolhe um tipo.
                tipo = Bloco.TERRA
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)

            if novo_bloco.tipo == 6:
                escadas_group.add(novo_bloco)
                escadas_linha.add(novo_bloco)
            else:
                blocos_group.add(novo_bloco)
                blocos_linha.add(novo_bloco)
                
    if linha > 10 and linha <= 200:
        for coluna in range(LARGURA):
            
            randomNumber = random.randint(0, 1000)
            
            # Criando um novo bloco:
            # Escolhe um tipo.
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.TERRA
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.FERRO
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.COBRE
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)
     
            blocos_group.add(novo_bloco)
            blocos_linha.add(novo_bloco)
    
    if linha > 200 and linha <= 350:
        for coluna in range(LARGURA):
            
            randomNumber = random.randint(0, 1000)
            
            # Criando um novo bloco:
            # Escolhe um tipo.
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.TERRA
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.FERRO
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.COBRE
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)
     
            blocos_group.add(novo_bloco)
            blocos_linha.add(novo_bloco)
            
    if linha > 350 and linha <= 600:
        for coluna in range(LARGURA):
            
            randomNumber = random.randint(0, 1000)
            
            # Criando um novo bloco:
            # Escolhe um tipo.
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.TERRA
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.FERRO
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.COBRE
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)
     
            blocos_group.add(novo_bloco)
            blocos_linha.add(novo_bloco)
            
    if linha > 600 and linha <= 850:
        for coluna in range(LARGURA):
            
            randomNumber = random.randint(0, 1000)
            
            # Criando um novo bloco:
            # Escolhe um tipo.
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.TERRA
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.FERRO
            if randomNumber >= 0 and randomNumber <=1000:
                tipo = Bloco.COBRE
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)
     
            blocos_group.add(novo_bloco)
            blocos_linha.add(novo_bloco)
            
    linha_sprites.append(blocos_linha)
    linha_sprites.append(escadas_linha)
    mapa.append(linha_sprites)
    


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
            
            
    #
    linhaJogador = minerador.rect.center[1] // TELA
    colunaJogador = minerador.rect.center[0] // TELA
    
    print(colunaJogador, linhaJogador)
    print(minerador.rect.x, minerador.rect.y)
            
    # Move o minerador pela tela.
    minerador.move()
    
    

    print(mapa[linhaJogador][0], mapa[linhaJogador][1])
    print(numeroEscadas)
            
    Colisao_Blocos(mapa)
    
    
    #Escadas
    
    numeroEscadas -= FazendoEscadas(numeroEscadas)
        
    numeroEscadas += Escadas_de_Volta()
        
    # Fim Escadas
    
                
    

    DISPLAYSURF.blit(fundo, (0, 0))    
    escadas_group.draw(DISPLAYSURF) 
    minerador_group.draw(DISPLAYSURF) 
    
    blocos_group.draw(DISPLAYSURF)    
    pygame.display.update()
    

