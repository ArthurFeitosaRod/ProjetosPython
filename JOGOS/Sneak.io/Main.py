import pygame               
from pygame.locals import *
import random

pygame.init()
#=========VARIAVEIS++++++++++
TELA_ALTURA = 400
TELA_LARGURA = 400
LARGURA_HEAD=20
ALTURA_HEAD=20
COBRA_HEAD = []
morreu = False
x = random.randint(40,380)
y = random.randint(40,398)
x_controle=20
y_controle=0
xc = TELA_LARGURA/2
yc = TELA_ALTURA/2
lista_cobra = []
comprimento_cobra = 5
clock = pygame.time.Clock()
pontos = 0
fonte = pygame.font.SysFont('Arial',30,True,True)
tela = pygame.display.set_mode((TELA_LARGURA,TELA_ALTURA))
#=============FUNÇOES++++++++++++
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x,y]
        #XeY[0] = x
        #XeY[1] = y
           
        pygame.draw.rect(tela, (0,255,0), (XeY[0],XeY[1], LARGURA_HEAD,ALTURA_HEAD))
def reiniciar_jogo():
    global pontos,morreu,comprimento_cobra,lista_cobra,x,y,xc,yc,lista_cabeca
    pontos = 0
    comprimento_cobra = 5
    xc = TELA_LARGURA/2
    yc = TELA_ALTURA/2
    lista_cabeca = []
    lista_cobra = []
    x = random.randint(40,380)
    y = random.randint(40,398)
    morreu = False
#=============RODAR_O_PROGRAMA+++++++++
while True:
    #=========Tempo++++++++++
    clock.tick(10)
    #==========Fonte+++++++++
    mensagem = f'pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    mensagemMorte = "GameOver(aperte R)"
    texto_formatadoMorte = fonte.render(mensagemMorte, True, (0,0,0))
#==============DESENHOS+++++++++++
    tela.fill((255,255,255))
    fruta = pygame.draw.rect(tela,(255,0,0),(x,y,18,18))
    COBRA_HEAD = pygame.draw.rect(tela,(0,255,0),(xc,yc,LARGURA_HEAD,ALTURA_HEAD))
#=============EVENTOS++++++++++++
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
        #========MOVIMENTO++++++++++
        """if pygame.key.get_pressed()[K_w]:
            yc -= 5
        if pygame.key.get_pressed()[K_s]:
            yc += 5
        if pygame.key.get_pressed()[K_a]:
            xc -= 5
        if pygame.key.get_pressed()[K_d]:
            xc += 5"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if y_controle == 20:
                    pass
                else:
                    y_controle = -20
                    x_controle = 0
            if event.key == pygame.K_s:
                if y_controle == -20:
                    pass
                else:
                    y_controle = 20
                    x_controle = 0
            if event.key == pygame.K_a:
                if x_controle == 20:
                    pass
                else:
                    x_controle = -20
                    y_controle = 0
            if event.key == pygame.K_d:
                if x_controle == -20:
                    pass
                else:
                    x_controle = 20
                    y_controle = 0
         
    xc = xc + x_controle
    yc = yc + y_controle       
    #===========CONDIÇÔES++++++++++
    if COBRA_HEAD.colliderect(fruta):
        x = random.randint(40,380)
        y = random.randint(40,398)
        comprimento_cobra += 10
        pontos = pontos + 1
    #=============LISTAS+++++++++++++
    lista_cabeca = []
    lista_cabeca.append(xc)
    lista_cabeca.append(yc)
    lista_cobra.append(lista_cabeca)
    aumenta_cobra(lista_cobra)
    if len(lista_cobra) > comprimento_cobra:
        del lista_cobra[0]
    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto_formatadoMorte, (50, 150))
            pygame.display.update()
    if xc > 395 or xc < 0 or yc > 395 or yc < 0:
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto_formatadoMorte, (50, 150))
            pygame.display.update()
    tela.blit(texto_formatado, (630,20))
    pygame.display.update() 
    