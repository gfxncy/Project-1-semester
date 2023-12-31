import pygame
import os
import sys
import random
import math
import ctypes
import tanks
import level
from music import music
from balls import Balls
pygame.init()
music()


BOARDSDENSITY = 1 / 2
ROTATIONSPEED = 5
AIMINGROTATIONSPEED = 1
TANKSPEED = 10
BACKSPEED = 10
N, M = 9, 6  # вертикальный и горизонтальные перекладинки)
SAFETIME = 12
BORDERWIDTH = 5
BULLETS = {"amount": 6, "radius": 6, "speed": 9, "dissapeartime": 500}
ROUNDS = 0
FPS = 50
BOOM = []
MUZZLE_ELONGETION = 10
size = width, height = 1520, 780
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
    'rotate_counterclockwise': pygame.K_RIGHT,
    'shoot': pygame.K_SPACE,
    'aming': pygame.K_m
}
buttons_2 = {
    'forward': pygame.K_w,
    'backward': pygame.K_s,
    'rotate_clockwise': pygame.K_a,
    'rotate_counterclockwise': pygame.K_d,
    'shoot': pygame.K_q,
    'aming': pygame.K_1
}

sounds1 = {"shoot": pygame.mixer.Sound('Music/nya.mp3')}
sounds2 = {"shoot": pygame.mixer.Sound('Music/nya2.mp3')}

borders = {'hor': horizontal_borders, 'ver': vertical_borders}

tank_group = pygame.sprite.Group()
AllTanks = [
    tanks.Tank(
        screen=screen,
        index=0,
        tankgroup=tank_group,
        spritegroup=all_sprites,
        buttons=buttons_1,
        speed=TANKSPEED,
        backspeed=BACKSPEED,
        rotationspeed=ROTATIONSPEED,
        borders=borders,
        sounds=sounds1,
        bullets=BULLETS,
        safetime=SAFETIME,
        boom=BOOM
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
        borders=borders,
        sounds=sounds2,
        bullets=BULLETS,
        safetime=SAFETIME,
        boom=BOOM
    )
]

for i in AllTanks:
    i.transfer()

def LivesCounter(mas):
    answer = 0
    for i in range(len(mas)):
        if mas[i].alive:
            answer += 1
    return answer

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
            if event.type == pygame.KEYDOWN:
                for i in range(len(AllTanks)):
                    if AllTanks[i].alive:
                        if event.key == AllTanks[i].buttons["shoot"]:
                            AllTanks[i].shoot()
                        if event.key == AllTanks[i].buttons["aming"]:
                            AllTanks[i].aming = True
                            pygame.mixer.music.pause()

            if event.type == pygame.KEYUP:
                for i in range(len(AllTanks)):
                    if AllTanks[i].alive:
                        if event.key == AllTanks[i].buttons["aming"]:
                            AllTanks[i].aming = False
                            pygame.mixer.music.unpause()

        #движение танков
        keys = pygame.key.get_pressed()
        for i in AllTanks:
            if i.alive:
                i.move(keys)

        #есть пробитие
        if LivesCounter(AllTanks) < 2:
            ROUNDS += 1
            Balls.empty()
            for i in AllTanks:
                i.bullets = 0
                i.transfer()

        #отрисовка объектов
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        all_sprites.update()

        if len(AllTanks) < 2:
            print(len(AllTanks))

        clock.tick(FPS)
        pygame.display.flip()