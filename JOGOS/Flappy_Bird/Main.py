import pygame
from pygame.locals import *
import os
import random
import neat

#VARIAVEIS
LARGURA = 288
ALTURA = 512
PONTOS = 0
#Inicializando
pygame.display.set_caption("FLAPPY BIRD")
pygame.init()
pygame.mixer.init()
#Variaveis
colidiu = False
cano_passou = False
pipe_gap = 100
ultimo_cano = pygame.time.get_ticks()
intervalo_cano = 1500 #milisegundos
x = 0
y = 0
começar = False
#DIRETORIOS

Diretorio_principal = os.path.dirname(__file__)
Diretorio_Audios = os.path.join(Diretorio_principal, "audio")
Diretorio_Imagens = os.path.join(Diretorio_principal, "sprites")

#Sons
som_passar = pygame.mixer.Sound(os.path.join(Diretorio_Audios, "point.ogg"))
som_passar.set_volume(1)
som_voar = pygame.mixer.Sound(os.path.join(Diretorio_Audios, "wing.ogg"))
som_voar.set_volume(1)
som_morte = pygame.mixer.Sound(os.path.join(Diretorio_Audios, "die.ogg"))
som_morte.set_volume(1)
som_hit = pygame.mixer.Sound(os.path.join(Diretorio_Audios, "hit.ogg"))
som_hit.set_volume(1)
#interface
tela = pygame.display.set_mode((LARGURA,ALTURA))
# Carregar imagens de números
numeros = {}
for i in range(10):
    numeros[str(i)] = pygame.image.load(os.path.join(Diretorio_Imagens, f"{i}.png"))
relogio = pygame.time.Clock()
#CLASSES
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_bird = []
        self.image_bird.append(pygame.image.load(os.path.join(Diretorio_Imagens, "redbird1.png")))
        self.image_bird.append(pygame.image.load(os.path.join(Diretorio_Imagens, "redbird2.png")))
        self.image_bird.append(pygame.image.load(os.path.join(Diretorio_Imagens, "redbird3.png")))
        self.atual = 1
        self.image = self.image_bird[self.atual]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA/2,300)
        self.velocidade = 0  
        self.gravidade = 1
        self.forca_pulo = -10
        self.angle = 0  
    def jump(self):
        self.velocidade = self.forca_pulo
        som_voar.play()
    def update(self):
        self.velocidade += self.gravidade
        self.rect.y += self.velocidade
        if self.velocidade < 0:
            self.angle = 25  # Ângulo olhando para cima
        else:
            self.angle -= 5
            if self.angle <= -90:
                self.angle = -90
        self.atual += 0.25
        self.image = self.image_bird[int(self.atual)]
        if self.atual >= 2:
            self.atual = 0

        self.image = pygame.transform.rotate(self.image, self.angle)  

       
        if self.rect.y > 380:
            self.rect.y = 380
            self.angle = -90 
        elif self.rect.y < 0:
            self.rect.y = 0
    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
class Chao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(Diretorio_Imagens, "base.png"))
        self.image1 = pygame.image.load(os.path.join(Diretorio_Imagens, "base.png"))
        self.rect = self.image.get_rect()
        self.rect1 = self.image1.get_rect()
        self.mask = pygame.mask.from_surface(self.image1)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = 400
        self.rect.x = 0
        self.rect1.y = 400
        self.rect1.x = LARGURA
    def update(self):
        self.rect.x -= 3
        self.rect1.x -= 3
        if self.rect.x + LARGURA < 0:
            self.rect.x = self.rect.x + LARGURA
        if self.rect1.x + LARGURA < 0:
            self.rect1.x = self.rect1.x + LARGURA
    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
        tela.blit(self.image1, self.rect1)
        self.update()
class Cano(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        #CANO NORMAL APONTADO PARA CIMA
        if pos == 1:
            self.image = pygame.image.load(os.path.join(Diretorio_Imagens, "pipe-green.png"))
            self.rect = self.image.get_rect()
            self.rect.topleft = [x,y + int(pipe_gap/2)]
        #VIRA O CANO APONTADO PARA BAIXO
        if pos == -1:
            self.image = pygame.image.load(os.path.join(Diretorio_Imagens, "pipe-green.png"))
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect()
            self.rect.bottomleft = [x,y - int(pipe_gap/2)]         
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        if self.rect.topright[0] < 0:
            self.kill()
            self.rect.x = LARGURA
        self.rect.x -= 5
        
    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
#Adicionar aos grupos
#defs
def Desenhar_tela(tela, birds, canos, Background, chao): # Dsenhar a tela sem os updates gigantescos
    tela.blit(Background, (0,0))
    chao.desenhar(tela) # Desenhar o chao
    for bird in birds: # Desenhar todos os pássaros IA tambem
        bird.desenhar(tela)
    for cano in canos: # todos os canos
        cano.desenhar(tela)
    pygame.display.update()
        
def criar_passaro():
    global bird_sprite
    bird_sprite.add(bird)
def desenhar_pontuacao(tela, pontos):
    str_pontos = str(min(pontos, 999))  # Limitar a pontuação a 999
    largura_total = sum(numeros[d].get_width() for d in str_pontos)
    
    # Posição inicial
    x_inicial = (LARGURA - largura_total) // 2
    y_inicial = 20  # distancia
    
    for digito in str_pontos:
        tela.blit(numeros[digito], (x_inicial, y_inicial))
        x_inicial += numeros[digito].get_width()
def eval_genoma(genoma, config):
    global colidiu,PONTOS,ultimo_cano,cano_passou,ge,redes,Tempo,bird
    Background = pygame.image.load(os.path.join(Diretorio_Imagens, 'background-day.png'))
    canos = [Cano(LARGURA,int(ALTURA/2) + random.randrange(-100,90),-1),
             Cano(LARGURA,int(ALTURA/2) + random.randrange(-100,90),1)]
    # grupo_colisao_atual = pygame.sprite.Group()
    chao = Chao()
        #grupo_colisao_atual.add(chao)
    Tempo = 30
    birds = [Bird()] # Passaros IA
    redes = []
    ge = []
    
    for _, genome in genoma:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        redes.append(net)
        genome.fitness = 0
        ge.append(genome)
        bird = Bird()
        birds.append(bird)
    altura_cano = random.randrange(-100,90) 
    cano_baixo = Cano(LARGURA,int(ALTURA/2) + altura_cano,-1)
    cano_cima = Cano(LARGURA,int(ALTURA/2) + altura_cano,1)
    # grupo_colisao_atual.add(cano_baixo, cano_cima)
    while True:
        relogio.tick(Tempo)
        tela.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == BUTTON_LEFT:  # Botão esquerdo do mouse
                    for bird in birds:
                        bird.jump()
                        som_voar.play()
        chao.update()
        #sistema de colisão
       # colisoes = pygame.sprite.spritecollide(bird, grupo_colisao, False, pygame.sprite.collide_mask)
        #Condiçoes
        for i, bird in enumerate(birds):
            bird.update()
            #ge[i].fitness += 0.1  # Recompensa por cada frame que
        # if len(canos) == 2:
        #     for cano in canos:
        #         if birds[0].rect.left > cano()[0].rect.left\
        #             and birds()[0].rect.right < cano()[0].rect.right\
        #             and cano_passou == False:
        #             cano_passou = True
        #         if cano_passou == True:
        #             if birds()[0].rect.right > cano()[0].rect.right:
        #                 PONTOS += 1
        #                 som_passar.play()
        #                 cano_passou = False         
        #Desenhar a imagem na tela
        Desenhar_tela(tela, birds, canos, Background, chao)
        desenhar_pontuacao(tela, PONTOS)
        pygame.display.update()
# Configuração do NEAT
def run(config_path):
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path)

    pop = neat.Population(config)
    pop.run(eval_genoma, 50)  # Executa o algoritmo NEAT por 50 gerações
    pop.add_reporter(neat.StdOutReporter(True))
    
if __name__ == "__main__":
    config_path = os.path.join(Diretorio_principal, 'config.txt')
    run(config_path)
    pygame.quit()