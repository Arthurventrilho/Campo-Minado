import pygame
import random
import time
from pygame.locals import *

TAMANHO = 40
LINHAS = 18
COLUNAS = 35

FPS = 30
 
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
pink = (255,0,255)

bright_red = (255,0,0)
bright_green = (0, 255, 0)
block_color = (53,115,255)
 
 
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
                elif coluna == tela.largura-2 and linha == posBandeira:
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
    
        sucesso = False
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
                    sucesso = True
        return sucesso
        
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
        
 
pygame.init()

tela = Tela(TAMANHO, LINHAS, COLUNAS)

gameDisplay = pygame.display.set_mode((tela.largurat, tela.alturat))
pygame.display.set_caption('Campo Minado')
clock = pygame.time.Clock()       
        
#Momentos do Jogo 
ESTADO_CAPA = 0
ESTADO_INSTRUCAO = 1
ESTADO_COMANDO = 2
ESTADO_PREPARO = 3
ESTADO_JOGO = 4
ESTADO_TERMINA = 5
ESTADO_GAME_OVER = 6
ESTADO_SUCESSO = 7
        
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
    
            largeText = pygame.font.Font('freesansbold.ttf',95)
            TextSurf, TextRect = text_objects1("CAMPO MINADO", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/3))
            gameDisplay.blit(TextSurf, TextRect)
            
            clicou_jogar = button("JOGAR", 150,450,100,50, green, bright_green)
            clicou_sair = button("SAIR", 550,450,100,50, red, bright_red)
            
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
            TextSurf1, TextRect = text_objects("Mine game consite em um jogo onde o objetivo é parmenecer", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/2.4))
            gameDisplay.blit(TextSurf1, TextRect)
            
            TextSurf2, TextRect = text_objects("vivo pelo máximo de tempo possível, mas tome cuidado", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/2))
            gameDisplay.blit(TextSurf2, TextRect)
            
            TextSurf3, TextRect = text_objects("se sua estamia acabar será GAME OVER", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/1.7))
            gameDisplay.blit(TextSurf3, TextRect)
            
            vai_para_configuration = button("Jogar", 350,450,100,50, green, bright_green)
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
     
    
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',80)
            TextSurf, TextRect = text_objects("TUDO PRONTO!", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/5))
            gameDisplay.blit(TextSurf, TextRect)
            
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf1, TextRect = text_objects("VAMOS VER SE VOCÊ", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/2.4))
            gameDisplay.blit(TextSurf1, TextRect)
            
            TextSurf2, TextRect = text_objects("TEM SORTE OU NÃO!", largeText)
            TextRect.center = ((tela.largurat/2),(tela.alturat/2))
            gameDisplay.blit(TextSurf2, TextRect)
            

            vai_para_jogo = button("Jogar", 350,380,100,50, green, bright_green)            
            if vai_para_jogo:
                GameExit = True
                print('')
                ESTADO = ESTADO_PREPARO
            
            pygame.display.update()
            clock.tick(FPS)  
            
    elif ESTADO == ESTADO_PREPARO:
        

        
        
        tempo = clock.tick(FPS)
        
        DISPLAYSURF = pygame.display.set_mode((tela.largurat, tela.alturat))
        
        fundo = pygame.image.load("fundo.jpg").convert()
        
 
        posJogador = random.randrange(4, tela.altura-2)
        posBandeira = random.randrange(4, tela.altura-2)
        # Cria minerador e adiciona em um grupo de Sprites.
        mineradorImagem = MineradorImagem("mineradorD.png", "mineradorE.png")
        minerador = Minerador(mineradorImagem.image1 , 100, 5, 1, 1 * 40, posJogador * 40 )
        minerador_group = pygame.sprite.Group()
        minerador_group.add(minerador)
        
        # Criando os blocos de minerio.       
        tela.criando()
        
        ESTADO = ESTADO_JOGO

        
    elif ESTADO == ESTADO_JOGO:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            
        if minerador.life <= 0:
            ESTADO = ESTADO_GAME_OVER
     
        # Move o minerador pela tela.
        minerador.move()
    
        sucesso = minerador.colisao_blocos(tela.blocos)
        if sucesso:
            ESTADO = ESTADO_SUCESSO
    
        DISPLAYSURF.blit(fundo, (0, 3 * 40))    
    
        tela.all.draw(DISPLAYSURF) 
        
        print(minerador.life)
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
                
                clicou_jogar_novamente = button("JOGAR", 150,450,100,50, green, bright_green)
                clicou_desistir = button("SAIR", 550,450,100,50, red, bright_red)
                
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
  
        
    

