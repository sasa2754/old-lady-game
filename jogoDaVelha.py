import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
meioLargura = largura/2
meioAltura = altura/2


tela = pygame.display.set_mode((largura,altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #inicio (x,começo), (x,fim), (tamanho da linha)
    pygame.draw.line(tela, (255,255,255), (420,0),(420,600), (5)) #vertical direita
    pygame.draw.line(tela, (255,255,255), (220,0),(220,600), (5)) #vertical esquerda
    pygame.draw.line(tela, (255,255,255), (0,160),(640,160), (5)) #horizontal cima
    pygame.draw.line(tela, (255,255,255), (0,325),(640,325), (5)) #horizontal baixo

    pygame.draw.circle(tela, (255,0,0), (meioLargura,meioAltura), 30) #centro
    pygame.draw.circle(tela, (255,0,0), (meioLargura+212,meioAltura), 30) #direita
    pygame.draw.circle(tela, (255,0,0), (meioLargura-212,meioAltura), 30) #esquerda
    pygame.draw.circle(tela, (255,0,0), (meioLargura,meioAltura-150), 30) #cima
    pygame.draw.circle(tela, (255,0,0), (meioLargura,meioAltura+150), 30) #baixo
    pygame.draw.circle(tela, (255,0,0), (meioLargura+212,meioAltura-150), 30) #superior direito
    pygame.draw.circle(tela, (255,0,0), (meioLargura-212,meioAltura-150), 30) #superior esquerdo
    pygame.draw.circle(tela, (255,0,0), (meioLargura+212,meioAltura+150), 30) #inferior direito
    pygame.draw.circle(tela, (255,0,0), (meioLargura-212,meioAltura+150), 30) #inferior esquerdo



    pygame.display.update()