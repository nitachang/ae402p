# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:29:17 2021

@author: nitac
"""




import pygame
import random
pygame.init()


screen=pygame.display.set_mode((500,600))
pygame.display.set_caption("我的遊戲")
done = False

clock = pygame.time.Clock()

PINK = pygame.color.Color("#FF00FB")
WHITE = (255,255,255)
BLACK = (0,0,0)

spaceship = pygame.image.load("spaceship.png").convert()
spaceship.set_colorkey(BLACK)
pygame.mixer.music.load('backgroundmusic.ogg')
lasersound=pygame.mixer.Sound('laser5.ogg')

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            lasersound.play()
            pygame.mixer.music.play()

            pos = pygame.mouse.get_pos()
    screen.fill(WHITE)
    
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    screen.blit(spaceship,(x,y))
    
    
    
    
    pygame.display.flip()
pygame.quit()
