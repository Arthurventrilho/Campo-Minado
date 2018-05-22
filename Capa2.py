import pygame
import time
pygame.init()
 
LARGURA = 800
ALTURA = 600
 
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0, 255, 0)
block_color = (53,115,255)
 

 
gameDisplay = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Mine Game')
clock = pygame.time.Clock()
 
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((LARGURA/2),(ALTURA/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()
    
    

def button(msg, x, y, w, h, ic, ac, action = None):
   mouse = pygame.mouse.get_pos() 
   click = pygame.mouse.get_pressed()
   
   if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "play":
                    game_loop()
                elif action == "quit":
                    pygame.quit()
                    quit()
                elif action == "Inst":
                    configuration()
   else:    
           pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
  
   smallText = pygame.font.Font("freesansbold.ttf",20)
   textSurf, textRect = text_objects(msg, smallText)
   textRect.center = ( (x+(w/2)), (y+(h/2)) )
   gameDisplay.blit(textSurf, textRect)

            

        
def game_intro():
    
    fundo = pygame.image.load("FUNDO.png")

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(fundo, (0,0))

        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("MINE GAME", largeText)
        TextRect.center = ((LARGURA/2),(ALTURA/3))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("JOGAR", 150,450,100,50, green, bright_green,"play")
        button("SAIR", 550,450,100,50, red, bright_red,"quit")
            
        pygame.display.update()
        clock.tick(15)
    
    

    
def game_loop():

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

    gameExit = False
 
    while not gameExit:
 
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
        
        button("Jogar", 350,450,100,50, green, bright_green,"Inst")
        
        pygame.display.update()
        clock.tick(120)    

game_intro()
game_loop()
pygame.quit()
quit()      