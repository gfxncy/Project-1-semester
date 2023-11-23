#концепция такая: змейка ползает не по квадратам
import pygame
import math

WIDTH = 800
HEIGHT = 600


#предпологается два класса только под змею: класс головы которая двигается как захочет игрок
#класс хвоста, который цепляется к голове и повторяет за ней все движения
class snake_head:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.min_speed = 10
        self.max_speed = 30
        self.r_curv = 100
        self.vx = 0
        self.vy = -2
        self.a_rad = 0.2
        self.ax = 0
        self.ay = 0
        self.color = (0, 0, 0)
        self.angle = 0
        self.turning_left = False
        self.turning_right = True
        


    def update_angle(self):
        self.angle = 0
        if not self.vx==0:
            self.angle = math.atan(self.vy/self.vx)
        elif self.vy>0:
            self.angle = math.pi/2
        else:
            self.angle = -1*math.pi/2
        if self.vx<0:
            self.angle += math.pi

    def move(self):
        self.update_angle()
        a_c = (self.vx**2 + self.vy**2)/(self.r_curv)
        if self.turning_left:
            self.vx+=a_c*math.cos(self.angle + math.pi/2)
            self.vy+=a_c*math.sin(self.angle + math.pi/2)
        if self.turning_right:
            self.vx+=a_c*math.cos(self.angle - math.pi/2)
            self.vy+=a_c*math.sin(self.angle - math.pi/2)


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


    def draw(self):
        h = 25
        w = 50
        d =  math.sqrt((w/2)**2 + (h/4)**2)
        a_0 = math.atan(h/(2*w))
        pygame.draw.polygon(self.screen, self.color, [[self.x + d*math.cos(-1*self.angle+a_0+math.pi), self.y+d*math.sin(-1*self.angle+a_0+math.pi)],
                                                     [self.x + d*math.cos(-1*self.angle-a_0-math.pi), self.y+d*math.sin(-1*self.angle-a_0-math.pi)],
                                                     [self.x - h/4 * math.sin(-1*self.angle), self.y + h/4 * math.cos(-1*self.angle)], 
                                                      [self.x - h/2 * math.sin(-1*self.angle), self.y + h/2 * math.cos(-1*self.angle)],
                                                      [self.x + w/2 * math.cos(-1*self.angle), self.y + w/2 * math.sin(-1*self.angle)],
                                                      [self.x + h/2 * math.sin(-1*self.angle), self.y - h/2 * math.cos(-1*self.angle)],
                                                      [self.x + h/4 * math.sin(-1*self.angle), self.y - h/4 * math.cos(-1*self.angle)]
                                                      ]

        )

    def boost(self, key):
        self.update_angle()
        


    
