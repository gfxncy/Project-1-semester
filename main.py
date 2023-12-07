import pygame
import os
import sys
import random
import math
import ctypes

pygame.init()

BOARDSDENSITY = 1 / 2
N, M = 9, 5
TANKSPEED = 7
BACKSPEED = 5
ROTATIONSPEED = 5
AIMINGROTATIONSPEED = 1
BALLSPEED = 9
DISAPPEARTIME = 500
RADIUS = 6
SAFETIME = 12
BORDERWIDTH = 5
BULLETS = 6
ROUNDS = 0
FPS = 50
BOOM = []
MUZZLE_ELONGETION = 10


size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)



all_sprites = pygame.sprite.Group()

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

def IsCorrect(x, y):
    return 0 <= x <= width and 0 <= y <= height

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        print(123)




Border(width/2, height/2-100, width/2, height/2+100)



if __name__ == '__main__':
    screen.fill(pygame.Color('white'))
    time = 0
    clock = pygame.time.Clock()

    running = True
    while running:  # главный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()

        clock.tick(FPS)
        pygame.display.flip()
