import pygame
import random
import time
from pygame.locals import *

LARGURA = 800
ALTURA = 600
 
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
    TextRect.center = ((LARGURA/2),(ALTURA/2))
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
        TextRect.center = ((LARGURA/2),(ALTURA/3))
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
        TextRect.center = ((LARGURA/2),(ALTURA/5))
        gameDisplay.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf1, TextRect = text_objects("Mine game consite em um jogo onde o objetivo é parmenecer", largeText)
        TextRect.center = ((LARGURA/2),(ALTURA/2.4))
        gameDisplay.blit(TextSurf1, TextRect)
        TextSurf2, TextRect = text_objects("vivo pelo máximo de tempo possível, mas tome cuidado", largeText)
        TextRect.center = ((LARGURA/2),(ALTURA/2))
        gameDisplay.blit(TextSurf2, TextRect)
        TextSurf3, TextRect = text_objects("se sua estamia acabar será GAME OVER", largeText)
        TextRect.center = ((LARGURA/2),(ALTURA/1.7))
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
        TextRect.center = ((LARGURA/2),(ALTURA/5))
        gameDisplay.blit(TextSurf, TextRect)
        largeText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf1, TextRect = text_objects("E - pega escada", largeText)
        TextRect.center = ((LARGURA/2),(ALTURA/2.4))
        gameDisplay.blit(TextSurf1, TextRect)
        TextSurf2, TextRect = text_objects("L - entra na loja", largeText)
        TextRect.center = ((LARGURA/2),(ALTURA/2))
        gameDisplay.blit(TextSurf2, TextRect)
        TextSurf3, TextRect = text_objects("S - entrar na casa para dormir", largeText)
        TextRect.center = ((LARGURA/2),(ALTURA/1.7))
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
        TextRect.center = ((LARGURA/2),(ALTURA/3))
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
        TextRect.center = ((LARGURA/2),(ALTURA/3))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("JOGAR", 150,450,100,50, green, bright_green,"play")
        button("SAIR", 550,450,100,50, red, bright_red,"quit")
            
        pygame.display.update()
        clock.tick(15)        

 
pygame.init()

gameDisplay = pygame.display.set_mode((LARGURA,ALTURA))
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
                    ESTADO = ESTADO_TERMINA
    
            gameDisplay.blit(capa, (0,0))
    
            largeText = pygame.font.Font('freesansbold.ttf',95)
            TextSurf, TextRect = text_objects1("CAMPO MINADO", largeText)
            TextRect.center = ((LARGURA/2),(ALTURA/3))
            gameDisplay.blit(TextSurf, TextRect)
            
            clicou_jogar = button("JOGAR", 150,450,100,50, green, bright_green)
            clicou_sair = button("SAIR", 550,450,100,50, red, bright_red)
            
            if clicou_jogar:
                intro = False
                ESTADO = ESTADO_INSTRUCAO
                
            if clicou_sair:
                intro = False
                ESTADO = ESTADO_TERMINA
                
            pygame.display.update()
            clock.tick(15)
   
    #Instruções
    elif ESTADO == ESTADO_INSTRUCAO:
        
        gameExit = False
        configurar_was_pressed = False
        
        while not gameExit:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ESTADO = ESTADO_TERMINA
    
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects("Sobre o jogo:", largeText)
            TextRect.center = ((LARGURA/2),(ALTURA/5))
            gameDisplay.blit(TextSurf, TextRect)
            
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf1, TextRect = text_objects("Mine game consite em um jogo onde o objetivo é parmenecer", largeText)
            TextRect.center = ((LARGURA/2),(ALTURA/2.4))
            gameDisplay.blit(TextSurf1, TextRect)
            
            TextSurf2, TextRect = text_objects("vivo pelo máximo de tempo possível, mas tome cuidado", largeText)
            TextRect.center = ((LARGURA/2),(ALTURA/2))
            gameDisplay.blit(TextSurf2, TextRect)
            
            TextSurf3, TextRect = text_objects("se sua estamia acabar será GAME OVER", largeText)
            TextRect.center = ((LARGURA/2),(ALTURA/1.7))
            gameDisplay.blit(TextSurf3, TextRect)
            
            vai_para_configuration = button("Jogar", 350,450,100,50, green, bright_green)
            if vai_para_configuration:
                gameExit = True
                ESTADO = ESTADO_COMANDO
            
            pygame.display.update()
            clock.tick(60)
    
    #Comando
    elif ESTADO == ESTADO_COMANDO:
        GameExit = False
        
        while not GameExit:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ESTADO = ESTADO_TERMINA
     
    
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',80)
            TextSurf, TextRect = text_objects("TUDO PRONTO!", largeText)
            TextRect.center = ((LARGURA/2),(ALTURA/5))
            gameDisplay.blit(TextSurf, TextRect)
            
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf1, TextRect = text_objects("VAMOS VER SE VOCÊ", largeText)
            TextRect.center = ((LARGURA/2),(ALTURA/2.4))
            gameDisplay.blit(TextSurf1, TextRect)
            
            TextSurf2, TextRect = text_objects("TEM SORTE OU NÃO!", largeText)
            TextRect.center = ((LARGURA/2),(ALTURA/2))
            gameDisplay.blit(TextSurf2, TextRect)
            

            vai_para_jogo = button("Jogar", 350,380,100,50, green, bright_green)            
            if vai_para_jogo:
                GameExit = True
                print('')
                ESTADO = ESTADO_SUCESSO
            
            pygame.display.update()
            clock.tick(80)  
            
    elif ESTADO == ESTADO_PREPARO:
        
            ESTADO = ESTADO_GAME_OVER
        
    elif ESTADO == ESTADO_JOGO:
        
            ESTADO = ESTADO_TERMINA
        
    elif ESTADO == ESTADO_TERMINA:
        
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
        
    elif ESTADO == ESTADO_GAME_OVER:
        
        tela_morreu = pygame.image.load("game_over.png")
    
        ge = False
        
        while not ge:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ESTADO = ESTADO_TERMINA
    
                gameDisplay.blit(tela_morreu, (0,0))
        
                largeText = pygame.font.Font('freesansbold.ttf',115)
                TextSurf, TextRect = text_objects1("GAME OVER", largeText)
                TextRect.center = ((LARGURA/2),(ALTURA/3))
                gameDisplay.blit(TextSurf, TextRect)
                
                clicou_jogar_novamente = button("JOGAR", 150,450,100,50, green, bright_green)
                clicou_desistir = button("SAIR", 550,450,100,50, red, bright_red)
                
                if clicou_jogar_novamente:
                    ge = True
                    ESTADO = ESTADO_PREPARO
                    
                if clicou_desistir:
                    ge = True
                    ESTADO = ESTADO_TERMINA
                    
                pygame.display.update()
                clock.tick(15)
          
        
    elif ESTADO == ESTADO_SUCESSO:
        
        boa = pygame.image.load("sucess.png")
    
        GE = False
        
        while not GE:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ESTADO = ESTADO_TERMINA
    
                gameDisplay.blit(boa, (0,0))
        
                largeText = pygame.font.Font('freesansbold.ttf',80)
                TextSurf, TextRect = text_objects1("PARABENS,", largeText)
                TextRect.center = ((LARGURA/2),(ALTURA/3))
                gameDisplay.blit(TextSurf, TextRect)
                
                largeText = pygame.font.Font('freesansbold.ttf',50)
                TextSurf1, TextRect = text_objects1("VOCÊ GANHOU!!", largeText)
                TextRect.center = ((LARGURA/2),(ALTURA/2.4))
                gameDisplay.blit(TextSurf1, TextRect)
                
                clicou_sucesso = button("JOGAR", 150,450,100,50, green, bright_green)
                clicou_quit = button("SAIR", 550,450,100,50, red, bright_red)
                
                if clicou_sucesso:
                    GE = True
                    ESTADO = ESTADO_PREPARO
                    
                if clicou_quit:
                    GE = True
                    ESTADO = ESTADO_TERMINA
                    
                pygame.display.update()
                clock.tick(15)
  
        
    

