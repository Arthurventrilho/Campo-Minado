import pygame
import random
from pygame.locals import *
                


def Colisao_Blocos():
    
    #Se o minerador bate nos blocos 
    for bloco in pygame.sprite.spritecollide(minerador, mapa[linhaJogador-1][0], False):
        bloco.life -= minerador.damage
        minerador.colide()
        if bloco.life <=0:
            bloco.kill()
    #Se o minerador bate nos blocos 
    for bloco in pygame.sprite.spritecollide(minerador, mapa[linhaJogador][0], False):
        bloco.life -= minerador.damage
        minerador.colide()
        if bloco.life <=0:
            bloco.kill()
    #Se o minerador bate nos blocos 
    for bloco in pygame.sprite.spritecollide(minerador, mapa[linhaJogador+1][0], False):
        bloco.life -= minerador.damage
        minerador.colide()
        if bloco.life <=0:
            bloco.kill()
            
            
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
        elif pressed_keys[K_UP] and pygame.sprite.spritecollide(minerador, mapa[linhaJogador - 1][1], False)\
            or pressed_keys[K_UP] and pygame.sprite.spritecollide(minerador, mapa[linhaJogador][1], False)\
            or pressed_keys[K_UP] and pygame.sprite.spritecollide(minerador, mapa[linhaJogador + 1][1], False):
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
minerador = Minerador("mineradorD.png", picareta1.damage, sapato1.speed, 200, 30*60, 15 * 40, (5 * 40) + 10 )
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
            
    linha_sprites.append(blocos_linha)
    linha_sprites.append(escadas_linha)
    mapa.append(linha_sprites)
    
for linha in range(ALTURA):
    blocos_linha = pygame.sprite.Group()
    if linha > 10 and linha <= 109:
        for coluna in range(LARGURA):
            # Criando um novo bloco:
            
            # Escolhe um tipo.
            randomNumber = random.randint(0, 1000)
           
            if randomNumber >= 0 and  randomNumber <=179:
                tipo = Bloco.FERRO
            elif randomNumber >= 180 and randomNumber <= 320:
                tipo = Bloco.COBRE
            else:
                tipo = Bloco.TERRA
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)
            blocos_linha.add(novo_bloco)
            blocos_group.add(novo_bloco)

    mapa.append(blocos_linha)
    
    
for linha in range(ALTURA):
    blocos_linha = pygame.sprite.Group()
    if linha >= 110 and linha <= 209:
        for coluna in range(LARGURA):
            # Criando um novo bloco:
            
            # Escolhe um tipo.
            randomNumber = random.randint(0, 1000)
            
            if randomNumber >= 0 and  randomNumber <=89:
                tipo = Bloco.OURO
            elif randomNumber >= 90 and  randomNumber <=189:
                tipo = Bloco.FERRO
            elif randomNumber >= 190 and randomNumber <= 320:
                tipo = Bloco.COBRE
            else:
                tipo = Bloco.TERRA
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)
            blocos_linha.add(novo_bloco)
            blocos_group.add(novo_bloco)

    mapa.append(blocos_linha)
    
for linha in range(ALTURA):
    blocos_linha = pygame.sprite.Group()
    if linha >= 210 and linha <= 509:
        for coluna in range(LARGURA):
            # Criando um novo bloco:
            
            # Escolhe um tipo.
            randomNumber = random.randint(0, 1000)
            
            if randomNumber >= 0 and  randomNumber <=89:
                tipo = Bloco.OURO
            elif randomNumber >= 90 and  randomNumber <=189:
                tipo = Bloco.FERRO
            elif randomNumber >= 190 and randomNumber <= 320:
                tipo = Bloco.COBRE
            elif randomNumber >= 321 and randomNumber <= 370:
               tipo = Bloco.RUBI
            else:
                tipo = Bloco.TERRA
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)
            blocos_linha.add(novo_bloco)
            blocos_group.add(novo_bloco)

    mapa.append(blocos_linha)
    
for linha in range(ALTURA):
    blocos_linha = pygame.sprite.Group()
    if linha >= 510 and linha <= ALTURA:
        for coluna in range(LARGURA):
            # Criando um novo bloco:
            
            # Escolhe um tipo.
            randomNumber = random.randint(0, 1000)
            
            if randomNumber >= 0 and  randomNumber <=89:
                tipo = Bloco.OURO
            elif randomNumber >= 90 and  randomNumber <=189:
                tipo = Bloco.FERRO
            elif randomNumber >= 190 and randomNumber <= 280:
                tipo = Bloco.COBRE
            elif randomNumber >= 280 and randomNumber <= 320:
               tipo = Bloco.RUBI
            elif randomNumber >= 321 and randomNumber <= 370:
               tipo = Bloco.DIAMANTE
            else:
                tipo = Bloco.TERRA
        
            # Calcula a posição.
            pos_x = coluna*TELA
            pos_y = linha*TELA
            
            # Cria o bloco e adiciona no mapa e no grupo.
            novo_bloco = Bloco(tipo, pos_x, pos_y)
            blocos_linha.add(novo_bloco)
            blocos_group.add(novo_bloco)

    mapa.append(blocos_linha)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
            
            
    #
    linhaJogador = minerador.rect.y // TELA
    colunaJogador = minerador.rect.x // TELA
    
    print(colunaJogador, linhaJogador)
    print(minerador.rect.x, minerador.rect.y)
            
    # Move o minerador pela tela.
    minerador.move()
    
    

    print(mapa[linhaJogador][0], mapa[linhaJogador][1])
    print(numeroEscadas)
            
    Colisao_Blocos()
    
    
    #FAzendo Esxcadas
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
        numeroEscadas -= 1
        
    numeroEscadas += Escadas_de_Volta()
        
        
        
    
    # Fim Escadas
                
    

    DISPLAYSURF.blit(fundo, (0, 0))    
    escadas_group.draw(DISPLAYSURF) 
    minerador_group.draw(DISPLAYSURF) 
    
    blocos_group.draw(DISPLAYSURF)    
    pygame.display.update()
    

