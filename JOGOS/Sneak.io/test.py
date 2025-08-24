import pygame
from pygame.locals import *
import random
import os

pygame.init()
TELA_LARGURA = 500
TELA_ALTURA = 600
x= 0
y= 300
yb = 0
xb = 150
pontos = 1
xb2 = 180
yb2 = 0
n= 90
largura = 85

                # FONTE DESEJAVEL, TAMANHO, NEGRITO(TRUE ou FALSE), ITÁLICO(TRUE ou FALSE)
fonte = pygame.font.SysFont('arial', 40 , True,True)
tela = pygame.display.set_mode((TELA_LARGURA,TELA_ALTURA))
bola2 = pygame.draw.circle(tela, (0,0,255), (xb2, yb2),15)
pygame.display.set_caption('jogo')

relogio = pygame.time.Clock()
    
while True:
    relogio.tick(n)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    GO = 'GAME OVER'
                        # QUEM, CERRILHAMENTO(PIXELs em TRUE Ou FALSE), COR(RGB)
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    texto_formatado2 = fonte.render(GO, True, (255,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
       # if event.type == KEYDOWN:
          #  if event.key == ord("a"):
         #       x -= 15
         #   if event.key == ord("s"):
          #      y += 15
         #   if event.key == ord("w"):
         #       y  -= 15
        ###    if event.key == ord("d"):
        ##        x += 15
        if pygame.key.get_pressed()[K_a]:
            x -= 15
        if pygame.key.get_pressed()[K_d]:
            x += 15
        if pygame.key.get_pressed()[K_w]:
            y -= 15
        if pygame.key.get_pressed()[K_s]:
            y += 15
          
                            #rgb            x , y , largura, altura
    player = pygame.draw.rect(tela, (255,255,255), (x,y,largura,20))
    bola = pygame.draw.circle(tela, (255,255,255), (xb, yb),15)
    if y >= TELA_ALTURA:
        y = 0
    if y < 0:
        y = (TELA_ALTURA - 1)
    if x >= TELA_LARGURA:
        x = 0
    if x < 0:
        x = (TELA_LARGURA - 1)
    if yb > TELA_ALTURA:
        yb = 0
    if yb2 > TELA_ALTURA:
        yb2 = 0
    if xb2 >= TELA_LARGURA:
        xb2 = 0
    if xb2 < 0:
        xb2 = (TELA_LARGURA - 1)
    yb += 4
    yb2 += 4
    xb2 += random.random()
    if player.colliderect(bola):
        yb = random.randint(0, 300)
        xb = random.randint(0,TELA_LARGURA)
        n += 1
        pontos += 1
    if n >= 100:
        bola2 = pygame.draw.circle(tela, (255,0,0), (xb2, yb2),15)
    if player.colliderect(bola2):
        yb2 = random.randint(0, 300)
        xb2 = random.randint(20, TELA_LARGURA)
        pontos = pontos -5
    if pontos <= 0:
                #texto com a fonte aplicada, x,y em tuplas
        tela.blit(texto_formatado2,(150, 250))
        c = 0
        for c in range(0, 10):
            pontos = 0
            n = 0
            xb = 0
            yb = 0
            x = 700
            y= 700
        
            # texto com a fonte aplicada, x,y em tuplas
    tela.blit(texto_formatado, (240,40))
    pygame.display.update()