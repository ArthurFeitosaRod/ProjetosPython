import pygame
from pygame.locals import *
import sys

pygame.init()
# Initialize Pygame
LARGURA = 250
ALTURA = 250
#Dimenção da janela
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Sprites')
#Classe
class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = []
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_1.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_2.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_3.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_4.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_5.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_6.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_7.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_8.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_9.png'))
        self.sprite.append(pygame.image.load('SAPO/animaçoes/attack_10.png'))
        self.atual = 0
        self.image = self.sprite[self.atual]
        self.image = pygame.transform.scale(self.image,(128*3,64*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 30, 60

    def update(self):
        self.atual = self.atual + 1
        if self.atual >= len(self.sprite):
            self.atual = 0
        self.image = self.sprite[self.atual]
        self.image = pygame.transform.scale(self.image,(128*3,64*3))
all_sprite = pygame.sprite.Group()
sapo = Sapo()
all_sprite.add(sapo)
relogio = pygame.time.Clock()
while True:
    relogio.tick(15)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    all_sprite.draw(tela)
    all_sprite.update()
    pygame.display.flip()
