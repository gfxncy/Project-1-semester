#концепция такая: змейка ползает не по квадратам
import pygame
import math

WIDTH = 800
HEIGHT = 600



class snake_head:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.min_speed = 10
        self.max_speed = 30
        self.r = 10
        self.vx = 2
        self.vy = 0
        self.a_rad = 0.2
        self.ax = 0
        self.ay = 0
        self.color = (0, 0, 0)
        self.angle = 0


    def update_angle(self):
        if not self.vx==0:
            self.angle = math.atan(self.vy/self.vx)
        else:
            self.angle = math.pi/2
        if self.vx<0:
            self.angle += math.pi

    def move(self):
        if self.x + self.vx < self.r:
            self.x  = WIDTH - self.r
        elif self.x + self.vx > WIDTH - self.r:
            self.x = self.r
        elif self.y - self.vy < self.r:
            self.y =  abs(self.y - self.vy) + self.r
        elif self.y - self.vy > HEIGHT - self.r:
            self.y =  HEIGHT - abs(HEIGHT - (self.y - self.vy)) - self.r
        else:
            self.x += self.vx
            self.y -= self.vy
        self.vx+=self.ax
        self.vy+=self.ay


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def boost(self, key):
        self.update_angle()
        


    
