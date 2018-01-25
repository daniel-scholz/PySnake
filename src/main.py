import sys
import time
from random import randint

import pygame
from pygame.locals import *

from src import db_connector, snake, my_text_input

scl = 25
width = height = 500
DISPLAY = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("PySnake")

# colors
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)
textBox = my_text_input.MyTextBox()
PAUSE = 0
RUNNING = 1


def opposite(k1, k2):
    if (k1 == K_DOWN and k2 == K_UP) or \
            (k1 == K_UP and k2 == K_DOWN) or \
            (k1 == K_LEFT and k2 == K_RIGHT) or (
            k1 == K_RIGHT and k2 == K_LEFT):
        return True


def pickLocation():
    food_p = [randint(0, width / scl - 1), randint(0, height / scl - 1)]
    food_p[0] *= scl
    food_p[1] *= scl
    return food_p


def endGame(s):
    textBox.show()
    db_connector.update_db(s.total, textBox.name)
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    last = pygame.K_RETURN
    food = pickLocation()
    s = snake.Snake()
    # gameloop
    while True:
        s.update()
        s.show()

        pygame.draw.rect(DISPLAY, pink, Rect(food[0], food[1], s.width, s.height))
        if s.eat(food):
            food = pickLocation()
        for t in s.tail:
            if s.eat(t):
                print("you lost")
                endGame(s)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                if not (s.vx == 0 and s.vy == 0):
                    endGame(s)
                pygame.quit()
                sys.exit()

            # movement
            if event.type == KEYDOWN:
                if not opposite(last, event.key):
                    if event.key == pygame.K_LEFT:
                        last = pygame.K_LEFT
                        s.setDir(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        last = pygame.K_RIGHT
                        s.setDir(1, 0)
                    elif event.key == pygame.K_UP:
                        last = pygame.K_UP
                        s.setDir(0, -1)
                    elif event.key == pygame.K_DOWN:
                        last = pygame.K_DOWN
                        s.setDir(0, 1)
        pygame.display.update()
        time.sleep(1 / (6 + s.total))


main()
