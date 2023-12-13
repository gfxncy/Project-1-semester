import random
import pygame
import math

import load_image
class Tank(pygame.sprite.Sprite):
    def __init__(self, screen, index, tankgroup, spritegroup, buttons, speed, backspeed, rotationspeed):
        super().__init__(tankgroup, spritegroup)
        self.angle = random.randrange(0, 360)
        self.angle_rad = self.angle * math.pi / 180
        self.width = 20 #половина ширины
        self.height = 20 #половина высоты

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
        self.rect = self.image.get_rect().move(500, 500)
        self.mask = pygame.mask.from_surface(self.image)

        self.buttons = buttons
        #buttons = {'forward': ..., 'backward': ..., 'rotate_clockwise': ..., 'rotate_counterclockwise': ...}
        #кнопки для перемещения танка

    def move(self, keys):
        """Перемещает танк, когда нажимают кнопки на клавиатуре"""
        x, y = 0, 0 #смещения после события

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

        #обновление координат и картинок
        self.rect.x += round(x)
        self.rect.y += round(y)
        self.image = pygame.transform.rotate(self.image_0, self.angle + 90)
        self.rect = self.image.get_rect(center=self.rect.center)
    def transfer(self):
        self.alive = True

        self.angle = random.randrange(0, 360)
        self.rect = self.image.get_rect().move(100, 100) #fixme добавить рандом координаты
        self.spritegroup.add(self)