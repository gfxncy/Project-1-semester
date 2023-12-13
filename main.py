import pygame
import os
import sys
import random
import math
import ctypes
import tanks

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


def IsCorrect(x, y):
    return 0 <= x <= width and 0 <= y <= height


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        if IsCorrect(x1, y1) and IsCorrect(x2, y2):
            super().__init__(all_sprites)
            if x1 == x2:  # вертикальная стенка
                self.add(vertical_borders)
                y2, y1 = max(y2, y1), min(y2, y1)
                self.image = pygame.Surface([BORDERWIDTH, y2 - y1])
                self.rect = pygame.Rect(x1, y1, BORDERWIDTH, y2 - y1)
                self.mask = pygame.mask.from_surface(self.image)
                if y2 - y1 != BORDERWIDTH - 4:
                    Border(x1 + 2, y1 + 2, x1 + BORDERWIDTH - 2, y1 + 2)
                    Border(x2 + 2, y2 - BORDERWIDTH - 2, x2 + BORDERWIDTH - 2, y2 - BORDERWIDTH - 2)
            else:  # горизонтальная стенка
                self.add(horizontal_borders)
                x2, x1 = max(x2, x1), min(x2, x1)
                self.image = pygame.Surface([x2 - x1, BORDERWIDTH])
                self.rect = pygame.Rect(x1, y1, x2 - x1, BORDERWIDTH)
                self.mask = pygame.mask.from_surface(self.image)
                if x2 - x1 != BORDERWIDTH - 4:
                    Border(x1 + 2, y1 + 2, x1 + 2, y1 + BORDERWIDTH - 2)
                    Border(x2 - BORDERWIDTH - 2, y2 + 2, x2 - BORDERWIDTH - 2, y2 + BORDERWIDTH - 2)


def make_perimetr():
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)


# "двумерный" массив превращается в.... стеночки! ура!
def generate_level(level):
    for i in range(len(level)):
        Border(*level[i])


# выдаёт true в среднем где-то probability раз из единицы
def decision(probability):
    return random.random() < probability


# эта функция для массивов размера (M-1)x(N-1), cгегерированных в new_level(), эта фкнция создаёт связи между элементами этого массива
# связь между элементами массива означает наличие стенки между координатами элементов этих массивов
# на выходе фунции "двумерный" массив, каждый элемент которого показывает с какими другими элементами он связан
def dfs(x, y):
    global color
    color[x][y][0] = 1
    m = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(len(m)):
        a = x + m[i][0]
        b = y + m[i][1]
        if 0 <= a <= N - 2 and 0 <= b <= M - 2:
            if color[a][b][0] == 0:
                if decision(BOARDSDENSITY):
                    color[x][y].append([a, b])
                    dfs(a, b)


# приобразование условных размеров, в которых генерируется карта, в размер экрана
def convert(x, y):
    return int(15 + (x + 1) * (width - 10) / N), int(5 + (y + 1) * (height - 10) / M)


# делаем новый уровень
def new_lewel():
    global color
    level = []

    # создаём список из пустых массивов размера (M-1)x(N-1)
    color = [[[0] for i in range(M - 1)] for j in range(N - 1)]

    # определяем с чем соединяем каждый элемент
    for i in range(len(color)):
        for j in range(len(color[i])):
            if color[i][j][0] == 0:
                dfs(i, j)

    # транформиркем структуру массива color и координаты
    for i in range(len(color)):
        for j in range(len(color[i])):
            for x in range(1, len(color[i][j])):
                a = convert(i, j)
                b = convert(color[i][j][x][0], color[i][j][x][1])
                level.append([a[0], a[1], b[0], b[1]])
    return level


# генерирует список стенок
level = new_lewel()
for i in range(len(color)): print(level[i])

# превращаем их в спрайты
generate_level(level)

make_perimetr()

# добавление танков в игру

buttons_1 = {
    'forward': pygame.K_UP,
    'backward': pygame.K_DOWN,
    'rotate_clockwise': pygame.K_LEFT,
    'rotate_counterclockwise': pygame.K_RIGHT
}

tank_group = pygame.sprite.Group()
AllTanks = [tanks.Tank(
    screen=screen,
    index=0,
    tankgroup=tank_group,
    spritegroup=all_sprites,
    buttons=buttons_1,
    speed=TANKSPEED,
    backspeed=BACKSPEED,
    rotationspeed=ROTATIONSPEED
)]

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