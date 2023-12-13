import random
import pygame
import math

import load_image
class Tank(pygame.sprite.Sprite):
    def __init__(self, screen, index, tankgroup, spritegroup):
        super().__init__(tankgroup, spritegroup)
        self.angle = random.randrange(0, 360)
        self.angle_rad = self.angle * math.pi / 180
        self.x = 500
        self.y = 500
        self.width = 20 #половина ширины
        self.height = 20 #половина высоты

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

        self.rect = self.image.get_rect().move(self.x, self.y)

    def transfer(self):
        self.alive = True

        self.angle = random.randrange(0, 360)
        self.rect = self.image.get_rect().move(self.x, self.y)
        self.spritegroup.add(self)