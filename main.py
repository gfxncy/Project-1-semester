import pygame
import os
import sys
import random
import math
import ctypes
import tanks
import level

pygame.init()

BOARDSDENSITY = 1 / 2
ROTATIONSPEED = 5
AIMINGROTATIONSPEED = 1
TANKSPEED = 10
BACKSPEED = 10
BALLSPEED = 9
N, M = 9, 6  # вертикальный и горизонтальные перекладинки)
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

params = level.level_param_param_purum_purum(width, height, BORDERWIDTH, BOARDSDENSITY, N, M)
horizontal_borders, vertical_borders = level.level_generator(params).get_borders()
all_sprites.add(horizontal_borders)
all_sprites.add(vertical_borders)
# добавление танков в игру

buttons_1 = {
    'forward': pygame.K_UP,
    'backward': pygame.K_DOWN,
    'rotate_clockwise': pygame.K_LEFT,
    'rotate_counterclockwise': pygame.K_RIGHT
}
buttons_2 = {
    'forward': pygame.K_w,
    'backward': pygame.K_s,
    'rotate_clockwise': pygame.K_a,
    'rotate_counterclockwise': pygame.K_d
}

borders = {'hor': horizontal_borders, 'ver': vertical_borders}

tank_group = pygame.sprite.Group()
AllTanks = [tanks.Tank(
    screen=screen,
    index=0,
    tankgroup=tank_group,
    spritegroup=all_sprites,
    buttons=buttons_1,
    speed=TANKSPEED,
    backspeed=BACKSPEED,
    rotationspeed=ROTATIONSPEED,
    borders=borders
    ),
    tanks.Tank(
        screen=screen,
        index=1,
        tankgroup=tank_group,
        spritegroup=all_sprites,
        buttons=buttons_2,
        speed=TANKSPEED,
        backspeed=BACKSPEED,
        rotationspeed=ROTATIONSPEED,
        borders=borders
    )
]

if __name__ == '__main__':

    # создание окна приложения
    screen.fill(pygame.Color('white'))
    time = 0
    clock = pygame.time.Clock()
    running = True

    #главный игровой цикл
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #движение танков
        keys = pygame.key.get_pressed()
        for i in AllTanks:
            if i.alive:
                i.move(keys)

        #отрисовка объектов
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()

        clock.tick(FPS)
        pygame.display.flip()