import pygame
import os
import game_module as gm
from abc import ABC, abstractmethod
from pygame.locals import RESIZABLE

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
win = pygame.display.set_mode(gm.SIZESCREEN, RESIZABLE)
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

run = True

fields = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


class Field(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join('png', 'rock.png'))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return self.image


def set_rock_fields():
    # stary algorytm, wyswietla rock fieldy
    x = 350
    y = 200
    for i in range(18):
        for j in range(10):
            win.blit(gm.ROCK_FIELD, (x, y))
            y += 60
        x += 60
        y = 200


def show_fields():
    # wyświetlanie fieldow z listy
    for i in range(18):
        for j in range(10):
            win.blit(fields[i][j].get_image(), (fields[i][j].get_x(), fields[i][j].get_y()))


def add_rocks_to_field_list():
    x = 350
    y = 200
    for i in range(18):
        for j in range(10):
            fields[i].insert(j, Field(x, y))
            y += 60
        x += 60
        y = 200


def redraw_game_window():
    win.blit(gm.bg, (0, 0))
    #set_rock_fields()
    show_fields()
    pygame.display.update()


add_rocks_to_field_list()
fields[0][0]
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False
    redraw_game_window()
pygame.quit()
