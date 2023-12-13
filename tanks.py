import random
import pygame
import math

import load_image
class Tank(pygame.sprite.Sprite):
    def __init__(self, screen, index, tankgroup, spritegroup, buttons, speed, backspeed, rotationspeed, borders):
        super().__init__(tankgroup, spritegroup)
        self.angle = random.randrange(0, 360)
        self.angle_rad = self.angle * math.pi / 180

        self.speed = speed
        self.backspeed = backspeed
        self.rotationspeed = rotationspeed

        self.screen = screen
        self.spritegroup = spritegroup
        self.tankgroup = tankgroup

        self.alive = True
        self.index = index

        if self.index == 0:
            self.image = load_image.load_image('tank_red.png')
            self.color = 'red'
        elif self.index == 1:
            self.image = load_image.load_image('tank_green.png')
            self.color = 'green'

        self.image_0 = self.image #изображение без вращения
        self.rect = self.image.get_rect().move(100, 100)
        self.mask = pygame.mask.from_surface(self.image)

        self.buttons = buttons
        #buttons = {'forward': ..., 'backward': ..., 'rotate_clockwise': ..., 'rotate_counterclockwise': ...}
        #кнопки для перемещения танка

        self.borders = borders

    def check_collision(self, horizontal_borders, vertical_borders):
        coll1 = False
        up_down = False
        coll2 = False
        left_right = False

        for i in horizontal_borders:
            offset = (i.rect.x - self.rect.x, i.rect.y - self.rect.y)
            if self.mask.overlap_area(i.mask, offset) > 0:
                coll1 = True
                if self.rect.centery < i.rect.y:
                    up_down = True
        for i in vertical_borders:
            offset = (i.rect.x - self.rect.x, i.rect.y - self.rect.y)
            if self.mask.overlap_area(i.mask, offset) > 0:
                coll2 = True
                if self.rect.centerx < i.rect.x:
                    left_right = True

        return coll1, coll2, up_down, left_right

    def move(self, keys):
        """Перемещает танк, когда нажимают кнопки на клавиатуре"""
        x, y = 0, 0 #смещения после события

        #проверка на столкновения

        coll1, coll2, up_down, left_right = self.check_collision(self.borders['hor'], self.borders['ver'])

        #обновление угла
        if keys[self.buttons['rotate_clockwise']]:
            self.angle += self.rotationspeed

        if keys[self.buttons['rotate_counterclockwise']]:
            self.angle -= self.rotationspeed

        self.angle = self.angle % 360

        #обновление координат
        if keys[self.buttons['forward']]:
            x = self.speed * math.cos(math.radians(self.angle))
            y = - self.speed * math.sin(math.radians(self.angle))

        if keys[self.buttons['backward']]:
            x = - self.backspeed * math.cos(math.radians(self.angle))
            y = self.backspeed * math.sin(math.radians(self.angle))

        #отмена движения при столкновении
        if coll1:
            if up_down:
                if y > 0:
                    y = 0
            else:
                if y < 0:
                    y = 0

        if coll2:
            if left_right:
                if x > 0:
                    x = 0
            else:
                if x < 0:
                    x = 0

        #обновление координат и картинок
        self.rect.x += round(x)
        self.rect.y += round(y)
        self.image = pygame.transform.rotate(self.image_0, self.angle + 90)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
    def transfer(self):
        self.alive = True

        self.angle = random.randrange(0, 360)
        self.rect = self.image.get_rect().move(100, 100) #fixme добавить рандом координаты
        self.spritegroup.add(self)