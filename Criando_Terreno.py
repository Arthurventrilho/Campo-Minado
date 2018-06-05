import pygame
import random
import time
from pygame.locals import *


 
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
pink = (255,0,255)
brown = (139,69,19)

bright_red = (255,0,0)
bright_green = (0, 255, 0)
block_color = (53,115,255)

#Momentos do Jogo 
ESTADO_CAPA = 0
ESTADO_INSTRUCAO = 1
ESTADO_COMANDO = 2
ESTADO_PREPARO = 3
ESTADO_JOGO = 4
ESTADO_TERMINA = 5
ESTADO_GAME_OVER = 6
ESTADO_SUCESSO = 7

#TIPOS DE BLOCO
TERRA = 0
DINAMITE_VISIVEL = 1
DINAMITE_INVISIVEL = 2
BANDEIRA = 3
GRANITO = 4
VIDA =5

#PARAMS DO MINERADOR
DANO = 1
SAUDE = 100
VELOCIDADE = 5

#tamnho da tile
TAMANHO = 40
#numero de linhas
LINHAS = 18
#numero de colunas
COLUNAS = 35

FPS = 30
 
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface1 = font.render(text, True, pink)
    return textSurface1, textSurface1.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((tela.largurat/2),(tela.alturat/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    
    
# Codigo adaptado de ...
def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos() 

    inside = False
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        inside = True
    
    if inside:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
    click = pygame.mouse.get_pressed()
    if inside and click[0] == 1:
        return True
    else:
        return False
        
def game_intro():
    
    capa = pygame.image.load("capa.png")

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(capa, (0,0))

        largeText = pygame.font.Font('freesansbold.ttf',105)
        TextSurf, TextRect = text_objects1("CAMPO MINADO", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/3))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("JOGAR", 150,450,100,50, green, bright_green,"play")
        button("SAIR", 550,450,100,50, red, bright_red,"quit")
            
        pygame.display.update()
        clock.tick(15)

    
def instrucao():

    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Sobre o jogo:", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/5))
        gameDisplay.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf1, TextRect = text_objects("Mine game consite em um jogo onde o objetivo é parmenecer", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/2.4))
        gameDisplay.blit(TextSurf1, TextRect)
        TextSurf2, TextRect = text_objects("vivo pelo máximo de tempo possível, mas tome cuidado", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/2))
        gameDisplay.blit(TextSurf2, TextRect)
        TextSurf3, TextRect = text_objects("se sua estamia acabar será GAME OVER", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/1.7))
        gameDisplay.blit(TextSurf3, TextRect)
        
        button("Jogar", 350,450,100,50, green, bright_green,"Inst")
        
        pygame.display.update()
        clock.tick(60)
        
        
def configuration():

    GameExit = False
 
    while not GameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Comando:", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/5))
        gameDisplay.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf1, TextRect = text_objects("E - pega escada", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/2.4))
        gameDisplay.blit(TextSurf1, TextRect)
        TextSurf2, TextRect = text_objects("L - entra na loja", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/2))
        gameDisplay.blit(TextSurf2, TextRect)
        TextSurf3, TextRect = text_objects("S - entrar na casa para dormir", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/1.7))
        gameDisplay.blit(TextSurf3, TextRect)
        
        button("Jogar", 350,450,100,50, green, bright_green,"bb")
        
        pygame.display.update()
        clock.tick(120)   
        
def game_over():
    
    tela_morreu = pygame.image.load("game_over.png")

    ge = False

    while ge:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(tela_morreu, (0,0))

        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects1("GAME OVER", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/3))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("JOGAR", 150,450,100,50, green, bright_green,"play")
        button("SAIR", 550,450,100,50, red, bright_red,"quit")
            
        pygame.display.update()
        clock.tick(180)

def sucess():
    
    boa = pygame.image.load("sucess.png")

    GE = False

    while GE:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(boa, (0,0))

        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects1("PARABÉSN, VOCÊ GANHOU!", largeText)
        TextRect.center = ((tela.largurat/2),(tela.alturat/3))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("JOGAR", 150,450,100,50, green, bright_green,"play")
        button("SAIR", 550,450,100,50, red, bright_red,"quit")
            
        pygame.display.update()
        clock.tick(15)        


# ===============      CLASSES      =============== 
class Tela():   
    def __init__(self, tamanhoBloco, altura, largura):
        self.tbloco = tamanhoBloco
        self.largura = largura
        self.altura = altura
        self.alturat = tamanhoBloco * altura
        self.largurat = tamanhoBloco * largura

        
    def criando(self):
        all_sprites = pygame.sprite.Group()
        posJogador = random.randrange(4, self.altura-2)
        posBandeira = random.randrange(4, self.altura-2)
        # Cria minerador e adiciona em um grupo de Sprites.
        minerador = Minerador( 1 * 40, posJogador * 40 )
        minerador_group = pygame.sprite.Group()
        minerador_group.add(minerador)
        all_sprites.add(minerador)
        blocos = pygame.sprite.Group()
        for linha in range(self.altura):
        
            for coluna in range(self.largura):
                tipo = - 1
                if linha == 0 or linha == (self.altura-1):
                    tipo = Bloco.GRANITO
                elif coluna == 0 or coluna == (self.largura-1):
                    tipo = Bloco.GRANITO
                elif coluna == 1 and linha == posJogador:
                    tipo = -1
                elif coluna == self.largura-2 and linha == posBandeira:
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
                    
        self.minerador = minerador
        self.all =  all_sprites
        self.blocos = blocos

class MineradorParams():
    def __init__(self, direita, esquerda, animacaoD, animacaoE, damage, speed, life):
        self.direita = pygame.image.load(direita)
        self.esquerda = pygame.image.load(esquerda)
        self.animD = pygame.image.load(animacaoD)
        self.animE = pygame.image.load(animacaoE)
        self.damage = damage
        self.speed = speed
        self.life = life
    

class Minerador(pygame.sprite.Sprite):
    
    params = MineradorParams("mineradorD.png", "mineradorE.png", "pica1.png", "pica1.png", DANO, VELOCIDADE, SAUDE)
    
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = Minerador.params.direita
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damage = Minerador.params.damage
        self.speed = Minerador.params.speed
        self.life = Minerador.params.life
        self.lastclock = pygame.time.get_ticks()
        self.cooldown = 200
        self.win = False
        self.lastrect = Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)

    def move(self):
        
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.image = Minerador.params.esquerda
            self.velocidadex = -self.speed
            self.velocidadey = 0
        elif pressed_keys[K_RIGHT]:
            self.image = Minerador.params.direita
            self.velocidadex = +self.speed
            self.velocidadey = 0
        elif pressed_keys[K_DOWN]:
            self.image = self.lastimage
            self.velocidadex = 0
            self.velocidadey = +self.speed
        elif pressed_keys[K_UP]:
            self.image = self.lastimage
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
            self.now = pygame.time.get_ticks()
            #se o personagem  estiver se movendo em x
            if (self.velocidadex != 0):
                #se ele estiver indo para a direita
                if (self.velocidadex > 0):
                    self.rect.right = bloco.rect.left
                    
                #se ele estiver indo para a esquerda
                elif (self.velocidadex < 0):
                    self.rect.left = bloco.rect.right
                    
                #ele para de na parede do bloco
                self.velocidadex = 0
                    
                
            #se estiver se movendo em y
            elif (self.velocidadey != 0):
                #se ele estiver indo para baixo
                if (self.velocidadey > 0):
                    self.rect.bottom = bloco.rect.top
                    
                #se ele estiver indo para cima
                elif (self.velocidadey < 0):
                    self.rect.top = bloco.rect.bottom
                
                #ele para de na parede do bloco
                self.velocidadey = 0
                
            self.hit(bloco)
        
    
    def hit(self, bloco):
        
        if self.now - self.lastclock >= self.cooldown:
            self.lastclock = self.now
            
            #animacao e som
            self.animacao()

    
            #blocos de graniso sao indestrutiveis
            if bloco.tipo != GRANITO:    
                bloco.life -= self.damage
            
            #se os blocos forem destruidos
            if bloco.life <=0:
                bloco.kill()
                #TNT
                if bloco.tipo == DINAMITE_VISIVEL:  
                    self.life -= 1
                #TNT escondida - morte
                if bloco.tipo == DINAMITE_INVISIVEL:  
                    self.life = 0
                #pega vida
                if bloco.tipo == VIDA:  
                    self.life += 1
                #ganha
                if bloco.tipo == BANDEIRA:  
                    self.win = True
                    
    def animacao(self):

        click = self.now
        if self.lastimage == Minerador.params.direita:
            self.image = Minerador.params.animD

                
            
        elif self.lastimage == Minerador.params.esquerda:
            self.image = Minerador.params.animE


    def update(self):
        volta = ESTADO_JOGO
        if tela.minerador.life <= 0:
            volta = ESTADO_GAME_OVER
     
        # Move o minerador pela tela.
        
        
        if self.image == Minerador.params.direita or self.image == Minerador.params.esquerda:
            self.lastimage = self.image
            
        if self.image == Minerador.params.animD or self.image == Minerador.params.animE:
            self.image = self.lastimage
            
        return volta
            
class BlocoParams:
    def __init__(self, image, vida):
        self.image = image
        self.life = vida

class Bloco(pygame.sprite.Sprite):
    
    TERRA = TERRA
    DINAMITE_VISIVEL = DINAMITE_VISIVEL
    DINAMITE_INVISIVEL = DINAMITE_INVISIVEL
    BANDEIRA = BANDEIRA
    GRANITO = GRANITO
    VIDA = VIDA

    
    tipos = {
        TERRA: BlocoParams(pygame.image.load("terra.png"), 3),
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
        
 
pygame.init()

tela = Tela(TAMANHO, LINHAS, COLUNAS)

gameDisplay = pygame.display.set_mode((tela.largurat, tela.alturat))
pygame.display.set_caption('Campo Minado')
clock = pygame.time.Clock()       
        

        
ESTADO = ESTADO_CAPA
while ESTADO != ESTADO_TERMINA:
    
    #CAPA
    if ESTADO == ESTADO_CAPA:
    
        capa = pygame.image.load("capa.png")
        
        intro = True
    
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            gameDisplay.blit(capa, (0,0))
    
            largeText = pygame.font.Font('freesansbold.ttf',110)
            TextSurf, TextRect = text_objects1("CAMPO MINADO", largeText,)
            TextRect.center = ((tela.largurat/2),(tela.alturat/3))
            gameDisplay.blit(TextSurf, TextRect)
            
            clicou_jogar = button("COMEÇAR", 450,450,150,75, green, bright_green)
            clicou_sair = button("SAIR", 850,450,150,75, red, bright_red)
            
            if clicou_jogar:
                intro = False
                ESTADO = ESTADO_INSTRUCAO
                
            if clicou_sair:
                intro = False
                pygame.quit()
                quit()
                
            pygame.display.update()
            clock.tick(FPS)
   
    #Instruções
    elif ESTADO == ESTADO_INSTRUCAO:
        
        gameExit = False
        configurar_was_pressed = False
        
        while not gameExit:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects("Sobre o jogo:", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/5))
            gameDisplay.blit(TextSurf, TextRect)
            
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf1, TextRect = text_objects("CAMPO MINADO é um jogo onde o objetivo é atravesar o mapa", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/2.4))
            gameDisplay.blit(TextSurf1, TextRect)
            
            TextSurf2, TextRect = text_objects("sem morrer, mas tome cuidado, o caminho ate la é perigoso,  ", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/2))
            gameDisplay.blit(TextSurf2, TextRect)
            
            TextSurf3, TextRect = text_objects("basta um passo em falso e sera GAME OVER ", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/1.7))
            gameDisplay.blit(TextSurf3, TextRect)
            
            vai_para_configuration = button("PROXIMO", 625,500,150,75, green, bright_green)
            if vai_para_configuration:
                gameExit = True
                ESTADO = ESTADO_COMANDO
            
            pygame.display.update()
            clock.tick(FPS)
    
    #Comando
    elif ESTADO == ESTADO_COMANDO:
        GameExit = False
        
        while not GameExit:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
     
            
            fotoComando = pygame.image.load("fotoComando.png")
            
            gameDisplay.blit(fotoComando, (0,0))
            largeText = pygame.font.Font('freesansbold.ttf',80)
            TextSurf, TextRect = text_objects1("TUDO PRONTO!", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/4.5))
            gameDisplay.blit(TextSurf, TextRect)
            
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf1, TextRect = text_objects1("QUE A SORTE  ", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/2.2))
            gameDisplay.blit(TextSurf1, TextRect)
            
            TextSurf2, TextRect = text_objects1("ESTEJA COM VOCE", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/1.8))
            gameDisplay.blit(TextSurf2, TextRect)
            

            vai_para_jogo = button("JOGAR", 625,550,150,75, green, bright_green)            
            if vai_para_jogo:
                GameExit = True
                print('')
                ESTADO = ESTADO_PREPARO
            
            pygame.display.update()
            clock.tick(FPS)  
            
    elif ESTADO == ESTADO_PREPARO:
        

        
        
        tempo = clock.tick(FPS)
        
        DISPLAYSURF = pygame.display.set_mode((tela.largurat, tela.alturat))
        
        fundo = pygame.Surface((tela.largurat, tela.alturat))
        fundo.fill(brown)
        
 

        
        # Criando os blocos de minerio.       
        tela.criando()
        
        ESTADO = ESTADO_JOGO

        
    elif ESTADO == ESTADO_JOGO:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        ESTADO = tela.minerador.update()    
        tela.minerador.move()
    
        tela.minerador.colisao_blocos(tela.blocos)
        if tela.minerador.win:
            ESTADO = ESTADO_SUCESSO
    
        DISPLAYSURF.blit(fundo, (0, 0))    
    
        tela.all.draw(DISPLAYSURF) 
        
        pygame.display.update()

        
    elif ESTADO == ESTADO_TERMINA:
        
        pygame.quit()
        quit()
        
    elif ESTADO == ESTADO_GAME_OVER:
        
        tela_morreu = pygame.image.load("game_over.png")
    
        ge = False
        
        while not ge:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
                gameDisplay.blit(tela_morreu, (0,0))
        
                largeText = pygame.font.Font('freesansbold.ttf',115)
                TextSurf, TextRect = text_objects1("GAME OVER", largeText)
                TextRect.center = ((tela.largurat/2),(tela.alturat/3))
                gameDisplay.blit(TextSurf, TextRect)
                
                clicou_jogar_novamente = button("RECOMEÇAR", 450,450,150,75, green, bright_green)
                clicou_desistir = button("SAIR", 850,450,150,75, red, bright_red)
                
                if clicou_jogar_novamente:
                    ge = True
                    ESTADO = ESTADO_PREPARO
                    
                if clicou_desistir:
                    ge = True
                    pygame.quit()
                    quit()
                    
                pygame.display.update()
                clock.tick(FPS)
          
        
    elif ESTADO == ESTADO_SUCESSO:
        
        boa = pygame.image.load("sucess.png")
    
        GE = False
        
        while not GE:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
                gameDisplay.blit(boa, (0,0))
        
                largeText = pygame.font.Font('freesansbold.ttf',80)
                TextSurf, TextRect = text_objects1("PARABENS,", largeText)
                TextRect.center = ((tela.largurat/2),(tela.alturat/3))
                gameDisplay.blit(TextSurf, TextRect)
                
                largeText = pygame.font.Font('freesansbold.ttf',50)
                TextSurf1, TextRect = text_objects1("VOCÊ GANHOU!!", largeText)
                TextRect.center = ((tela.largurat/2),(tela.alturat/2.4))
                gameDisplay.blit(TextSurf1, TextRect)
                
                clicou_sucesso = button("JOGAR", 150,450,100,50, green, bright_green)
                clicou_quit = button("SAIR", 550,450,100,50, red, bright_red)
                
                if clicou_sucesso:
                    GE = True
                    ESTADO = ESTADO_PREPARO
                    
                if clicou_quit:
                    GE = True
                    pygame.quit()
                    quit()
                    
                pygame.display.update()
                clock.tick(FPS)
  
        
    


