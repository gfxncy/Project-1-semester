import math
from random import choice
from random import randint as rnd
from snake_parts import * 
import pygame


FPS = 60

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()

finished = False
snake_head1 = snake_head(screen=screen, x=WIDTH/2, y=HEIGHT/2)
while not finished:
    screen.fill(WHITE)
    snake_head1.move()
    snake_head1.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        #elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_UP:
                #snake_head1.acceleration_positive()
            #elif event.key == pygame.K_DOWN:
                #snake_head1.acceleration_negative()
       # elif event.type == pygame.KEYUP:
            #if event.key == pygame.K_UP:
                #snake_head1.acceleration_negative()
            #elif event.key == pygame.K_DOWN:
                #snake_head1.acceleration_positive()
    pygame.time.Clock()
        


pygame.quit()
