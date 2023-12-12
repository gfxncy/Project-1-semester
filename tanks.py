import random
import pygame as pg
import math

class Tank:
    def __init__(self, color, screen):
        self.angle = random.randrange(0, 360)
        self.angle_rad = self.angle * math.pi / 180
        self.x = 0
        self.y = 0
        self.width = 20 #половина ширины
        self.height = 20 #половина высоты

        self.screen = screen
        self.color = color
        self.alive = True

    def draw(self):
        #точки полигона
        phi = self.angle_rad
        w = self.width
        h = self.height
        p1 = (self.x + w * math.cos(phi) - h * math.sin(phi), self.y + w * math.sin(phi) + h * math.cos(phi))
        p2 = (self.x - w * math.cos(phi) - h * math.sin(phi), self.y - w * math.sin(phi) + h * math.cos(phi))
        p3 = (self.x - w * math.cos(phi) + h * math.sin(phi), self.y - w * math.sin(phi) - h * math.cos(phi))
        p4 = (self.x + w * math.cos(phi) + h * math.sin(phi), self.y + w * math.sin(phi) - h * math.cos(phi))
        pg.draw.polygon(self.screen, self.color, (p1, p2, p3, p4))