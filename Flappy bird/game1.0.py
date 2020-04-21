import pygame
from pygame.locals import *
from sys import exit

pygame.init()

img_background = "beach.png"
img_fish = "fish.png"
img_pole = "pole.png"
move_x = 0
move_y = 0
x = 200
y = 300
FPS = 60
REFRESH = 5
pipe_x = 800
pipe_y = 300
bot_pipes = []
top_pipes = []
#background_position = (0,0)

pygame.mouse.set_visible(False)
reloj = pygame.time.Clock()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Flappy Whale")

background = pygame.image.load(img_background).convert()
background = pygame.transform.scale(background, (800, 600))

cursor = pygame.image.load(img_fish).convert_alpha()
cursor = pygame.transform.scale(cursor, (60, 60))

pipe = pygame.image.load(img_pole).convert_alpha()
pipe = pygame.transform.scale(pipe, (85, 300))

def esperarTeclaJugador():
  while True:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        exit()
      if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE: # Quita al presionar ESCAPE
            pygame.quit()
            exit()
        return
    

screen.blit(background, (move_x, move_y))  
#screen.blit(pipe, (720,0))
screen.blit(cursor, (x,y))  
#screen.blit(pipe, (pipe_x,pipe_y))
pygame.display.update()
esperarTeclaJugador()

while True:
    #Captura de eventos########################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Quita al presionar ESCAPE
              pygame.quit()
              exit()   
            if event.key == pygame.K_UP:
                move_y = -10
    ###########################################################################
    #Efecto de caida del personaje#############################################
    move_y += 1
    y += move_y    
    if y >= (background.get_height()-60):
        y = background.get_height()-60
    elif y <= 0:
        y = 0
    ###########################################################################
    #Transicion del fondo######################################################
    if (REFRESH == 0):
        move_x -= 3
        REFRESH = 5
        
    screen.blit(background, (move_x, 0))    
    if move_x >= (-800):
        screen.blit(background, ((800+move_x),0))
    else :
       move_x = 0
    ###########################################################################
    #Generar pipes

    pipe_x -= 4
    if pipe_x <= -85 :
        pipe_x = 800
    #if pipe_x == 400:
        
    screen.blit(pipe, (pipe_x,pipe_y))
    ###########################################################################
    
    screen.blit(cursor, (x,y))    
    reloj.tick(FPS)
    REFRESH -= 1
    pygame.display.update()
