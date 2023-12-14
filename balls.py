import random
import pygame
import math
from level import vertical_borders, horizontal_borders

Balls = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, vx, vy, parent, spiritgroup, TIME):
        super().__init__(spiritgroup)
        self.add(Balls)
        self.time = 0
        self.DieTime = TIME
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("black"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.mask = pygame.mask.from_surface(self.image)
        self.vx = vx
        self.vy = vy
        self.vx0 = vx
        self.vy0 = vy
        self.up_down = self.vy0 <= 0
        self.left_right = self.vx0 <= 0
        self.parent = parent

    def update(self):
        self.time += 1
        if self.time >= self.DieTime:
            self.parent.Counter[0] -= 1
            self.kill()

        coll1 = False
        up_down = False
        coll2 = False
        left_right = False

        for i in horizontal_borders:
            offset = (i.rect.x - self.rect.x, i.rect.y - self.rect.y)
            if self.mask.overlap_area(i.mask, offset) > 0:
                coll1 = True
                if self.rect.centery <= i.rect.y:
                    up_down = True
        for i in vertical_borders:
            offset = (i.rect.x - self.rect.x, i.rect.y - self.rect.y)
            if self.mask.overlap_area(i.mask, offset) > 0:
                coll2 = True
                if self.rect.centerx <= i.rect.x:
                    left_right = True

        if coll1:
            if up_down:
                if not self.up_down:
                    self.vy = -self.vy0
                else:
                    self.vy = self.vy0
            else:
                if self.up_down:
                    self.vy = -self.vy0
                else:
                    self.vy = self.vy0
        if coll2:
            if left_right:
                if not self.left_right:
                    self.vx = -self.vx0
                else:
                    self.vx = self.vx0
            else:
                if self.left_right:
                    self.vx = -self.vx0
                else:
                    self.vx = self.vx0

        self.rect = self.rect.move(self.vx, self.vy)


def rot_center(image, rect, angle):
    rotated_image = pygame.transform.rotate(image, angle + 90)
    new_rect = rotated_image.get_rect(center=rect.center)
    new_mask = pygame.mask.from_surface(rotated_image)

    return rotated_image, new_rect, new_mask