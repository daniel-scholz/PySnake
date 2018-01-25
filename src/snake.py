from random import randint

import pygame

from src import main

import math


class Snake:
    def __init__(self):
        self.px = 0
        self.py = 0
        self.vx = 0
        self.vy = 0
        self.width = self.height = 25
        self.total = 0
        self.tail = []
        self.tail_colour = []

    def update(self):
        if len(self.tail) == self.total:
            for i in range(len(self.tail) - 1):
                self.tail[i] = self.tail[i + 1]
            if len(self.tail) != 0:
                self.tail[-1] = [self.px, self.py]
        else:
            self.tail.append([self.px, self.py])
            self.tail_colour.append(randint(0, 255))
        self.px += self.vx * main.scl
        self.py += self.vy * main.scl
        if self.px >= main.width:
            self.px = 0
        # left border collison handling
        if self.px < 0:
            self.px = main.width - self.width

        # top border collison handling
        if self.py >= main.height:
            self.py = 0

        # bottom border collison handling
        if self.py < 0:
            self.py = main.height - self.height

    def show(self):
        # wipe screen
        main.DISPLAY.fill((51, 51, 51))
        pygame.draw.rect(main.DISPLAY, (255, 255, 255),
                         pygame.Rect(self.px, self.py, self.height, self.width))

        c1 = (randint(0, 255), randint(0, 255), randint(0, 255))
        c2 = (randint(0, 255), randint(0, 255), randint(0, 255))
        # uncomment for colourful blinking snake
        for i in range(len(self.tail)):
            # pygame.draw.rect(Main.DISPLAY, (0, self.tail_colour[i], 0),
            # pygame.Rect(self.tail[i][0], self.tail[i][1], self.height, self.width))
            if i % 2 == 0:
                pygame.draw.rect(main.DISPLAY, c1,
                                 pygame.Rect(self.tail[i][0], self.tail[i][1], self.height, self.width))
            else:
                pygame.draw.rect(main.DISPLAY, c2,
                                 pygame.Rect(self.tail[i][0], self.tail[i][1], self.height, self.width))

    def setDir(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def eat(self, food):
        d = math.sqrt((food[0] - self.px) ** 2 + (food[1] - self.py) ** 2)
        if d <= 1:
            self.total += 1
            print("%d FPS" % (self.total + 6))
            return True
        else:
            return False