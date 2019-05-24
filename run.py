import pygame
import os
import game_module as gm
from pygame.locals import RESIZABLE

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
win = pygame.display.set_mode(gm.SIZESCREEN, RESIZABLE)
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

run = True

fields = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
yellow_fields = []


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *groups):
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.image = image

    def draw(self, image):
        win.blit(image, (self.x, self.y))

    def can_go_left(self):
        for i in range(len(yellow_fields)):
            if yellow_fields[i].x == self.x - 60 and yellow_fields[i].y == self.y:
                return True

    def can_go_right(self):
        for i in range(len(yellow_fields)):
            if yellow_fields[i].x == self.x + 60 and yellow_fields[i].y == self.y:
                return True

    def can_go_up(self):
        for i in range(len(yellow_fields)):
            if yellow_fields[i].x == self.x and yellow_fields[i].y == self.y - 60:
                return True

    def can_go_down(self):
        for i in range(len(yellow_fields)):
            if yellow_fields[i].x == self.x and yellow_fields[i].y == self.y + 60:
                return True

   # def move(self):
        # for coordinates in yellow_fields:
            # if [self.x, self.y] in yellow_fields:


class Field(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = gm.ROCK_FIELD

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image


class YellowField(Field):
    def __init__(self, x, y, visible):
        super().__init__(x, y)
        self.visible = visible
        self.image = gm.YELLOW_FIELD

    def get_visible(self):
        return self.visible


def draw_final_fields():
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


def set_lvl_1_fields():
    fields[0][3].set_image(gm.BLACK_FIELD)
    fields[0][4].set_image(gm.BLACK_FIELD)
    fields[0][5].set_image(gm.BLACK_FIELD)
    fields[0][6].set_image(gm.BLACK_FIELD)
    fields[0][8].set_image(gm.BLACK_FIELD)
    fields[0][9].set_image(gm.BLACK_FIELD)
    fields[1][3].set_image(gm.BLACK_FIELD)
    fields[1][4].set_image(gm.BLACK_FIELD)
    fields[1][9].set_image(gm.BLACK_FIELD)
    fields[2][9].set_image(gm.BLACK_FIELD)
    fields[3][9].set_image(gm.BLACK_FIELD)
    fields[4][0].set_image(gm.BLACK_FIELD)
    fields[5][0].set_image(gm.BLACK_FIELD)
    fields[5][9].set_image(gm.BLACK_FIELD)
    fields[6][0].set_image(gm.BLACK_FIELD)
    fields[6][9].set_image(gm.BLACK_FIELD)
    fields[7][0].set_image(gm.BLACK_FIELD)
    fields[7][9].set_image(gm.BLACK_FIELD)
    fields[8][0].set_image(gm.BLACK_FIELD)
    fields[9][9].set_image(gm.BLACK_FIELD)
    fields[10][9].set_image(gm.BLACK_FIELD)
    fields[11][8].set_image(gm.BLACK_FIELD)
    fields[11][9].set_image(gm.BLACK_FIELD)
    fields[12][7].set_image(gm.BLACK_FIELD)
    fields[12][8].set_image(gm.BLACK_FIELD)
    fields[12][9].set_image(gm.BLACK_FIELD)
    fields[12][9].set_image(gm.BLACK_FIELD)
    fields[13][0].set_image(gm.BLACK_FIELD)
    fields[13][7].set_image(gm.BLACK_FIELD)
    fields[13][8].set_image(gm.BLACK_FIELD)
    fields[13][9].set_image(gm.BLACK_FIELD)
    fields[14][7].set_image(gm.BLACK_FIELD)
    fields[14][8].set_image(gm.BLACK_FIELD)
    fields[14][9].set_image(gm.BLACK_FIELD)
    fields[15][8].set_image(gm.BLACK_FIELD)
    fields[15][9].set_image(gm.BLACK_FIELD)
    fields[16][9].set_image(gm.BLACK_FIELD)
    fields[17][0].set_image(gm.BLACK_FIELD)
    fields[17][4].set_image(gm.BLACK_FIELD)
    fields[17][5].set_image(gm.BLACK_FIELD)
    fields[17][8].set_image(gm.BLACK_FIELD)
    fields[17][9].set_image(gm.BLACK_FIELD)

    yellow_fields.append(YellowField(fields[0][1].get_x(), fields[0][1].get_y(), True))
    yellow_fields.append(YellowField(fields[1][1].get_x(), fields[1][1].get_y(), True))
    yellow_fields.append(YellowField(fields[2][1].get_x(), fields[2][1].get_y(), True))
    yellow_fields.append(YellowField(fields[3][1].get_x(), fields[3][1].get_y(), True))
    yellow_fields.append(YellowField(fields[3][2].get_x(), fields[3][2].get_y(), True))
    yellow_fields.append(YellowField(fields[3][3].get_x(), fields[3][3].get_y(), True))
    yellow_fields.append(YellowField(fields[3][5].get_x(), fields[3][5].get_y(), True))
    yellow_fields.append(YellowField(fields[3][7].get_x(), fields[3][7].get_y(), True))
    yellow_fields.append(YellowField(fields[4][3].get_x(), fields[4][3].get_y(), True))
    yellow_fields.append(YellowField(fields[4][5].get_x(), fields[4][5].get_y(), True))
    yellow_fields.append(YellowField(fields[4][7].get_x(), fields[4][7].get_y(), True))
    yellow_fields.append(YellowField(fields[4][8].get_x(), fields[4][8].get_y(), True))
    yellow_fields.append(YellowField(fields[5][1].get_x(), fields[5][1].get_y(), True))
    yellow_fields.append(YellowField(fields[5][2].get_x(), fields[5][2].get_y(), True))
    yellow_fields.append(YellowField(fields[5][3].get_x(), fields[5][3].get_y(), True))
    yellow_fields.append(YellowField(fields[5][4].get_x(), fields[5][4].get_y(), True))
    yellow_fields.append(YellowField(fields[5][5].get_x(), fields[5][5].get_y(), True))
    yellow_fields.append(YellowField(fields[5][7].get_x(), fields[5][7].get_y(), True))
    yellow_fields.append(YellowField(fields[6][2].get_x(), fields[6][2].get_y(), True))
    yellow_fields.append(YellowField(fields[6][5].get_x(), fields[6][5].get_y(), True))
    yellow_fields.append(YellowField(fields[6][7].get_x(), fields[6][7].get_y(), True))
    yellow_fields.append(YellowField(fields[7][2].get_x(), fields[7][2].get_y(), True))
    yellow_fields.append(YellowField(fields[7][5].get_x(), fields[7][5].get_y(), True))
    yellow_fields.append(YellowField(fields[7][7].get_x(), fields[7][7].get_y(), True))
    yellow_fields.append(YellowField(fields[8][2].get_x(), fields[8][2].get_y(), True))
    yellow_fields.append(YellowField(fields[8][5].get_x(), fields[8][5].get_y(), True))
    yellow_fields.append(YellowField(fields[8][7].get_x(), fields[8][7].get_y(), True))
    yellow_fields.append(YellowField(fields[8][8].get_x(), fields[8][8].get_y(), True))
    yellow_fields.append(YellowField(fields[9][1].get_x(), fields[9][1].get_y(), True))
    yellow_fields.append(YellowField(fields[9][2].get_x(), fields[9][2].get_y(), True))
    yellow_fields.append(YellowField(fields[9][3].get_x(), fields[9][3].get_y(), True))
    yellow_fields.append(YellowField(fields[9][5].get_x(), fields[9][5].get_y(), True))
    yellow_fields.append(YellowField(fields[9][7].get_x(), fields[9][7].get_y(), True))
    yellow_fields.append(YellowField(fields[10][1].get_x(), fields[10][1].get_y(), True))
    yellow_fields.append(YellowField(fields[10][3].get_x(), fields[10][3].get_y(), True))
    yellow_fields.append(YellowField(fields[10][5].get_x(), fields[10][5].get_y(), True))
    yellow_fields.append(YellowField(fields[10][6].get_x(), fields[10][6].get_y(), True))
    yellow_fields.append(YellowField(fields[10][7].get_x(), fields[10][7].get_y(), True))
    yellow_fields.append(YellowField(fields[11][1].get_x(), fields[11][1].get_y(), True))
    yellow_fields.append(YellowField(fields[12][1].get_x(), fields[12][1].get_y(), True))
    yellow_fields.append(YellowField(fields[12][2].get_x(), fields[12][2].get_y(), True))
    yellow_fields.append(YellowField(fields[12][3].get_x(), fields[12][3].get_y(), True))
    yellow_fields.append(YellowField(fields[12][4].get_x(), fields[12][4].get_y(), True))
    yellow_fields.append(YellowField(fields[12][5].get_x(), fields[12][5].get_y(), True))
    yellow_fields.append(YellowField(fields[12][6].get_x(), fields[12][6].get_y(), True))
    yellow_fields.append(YellowField(fields[13][3].get_x(), fields[13][3].get_y(), True))
    yellow_fields.append(YellowField(fields[13][5].get_x(), fields[13][5].get_y(), True))
    yellow_fields.append(YellowField(fields[14][1].get_x(), fields[14][1].get_y(), True))
    yellow_fields.append(YellowField(fields[14][3].get_x(), fields[14][3].get_y(), True))
    yellow_fields.append(YellowField(fields[14][5].get_x(), fields[14][5].get_y(), True))
    yellow_fields.append(YellowField(fields[15][1].get_x(), fields[15][1].get_y(), True))
    yellow_fields.append(YellowField(fields[15][3].get_x(), fields[15][3].get_y(), True))
    yellow_fields.append(YellowField(fields[15][5].get_x(), fields[15][5].get_y(), True))
    yellow_fields.append(YellowField(fields[15][6].get_x(), fields[15][6].get_y(), True))
    yellow_fields.append(YellowField(fields[16][1].get_x(), fields[16][1].get_y(), True))
    yellow_fields.append(YellowField(fields[16][2].get_x(), fields[16][2].get_y(), True))
    yellow_fields.append(YellowField(fields[16][3].get_x(), fields[16][3].get_y(), True))
    yellow_fields.append(YellowField(fields[16][6].get_x(), fields[16][6].get_y(), True))
    yellow_fields.append(YellowField(fields[16][7].get_x(), fields[16][7].get_y(), True))
    yellow_fields.append(YellowField(fields[16][8].get_x(), fields[16][8].get_y(), True))


def draw_yellow_fields():
    for field in yellow_fields:
        if field.get_visible():
            win.blit(field.get_image(), (field.get_x(), field.get_y()))


def redraw_game_window():
    win.blit(gm.bg, (0, 0))
    draw_final_fields()
    draw_yellow_fields()
    ghost.draw(gm.STAND_U)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_LEFT] and ghost.can_go_left():
        ghost.x -= 60
        ghost.draw(gm.STAND_L)
    if keys[pygame.K_RIGHT] and ghost.can_go_right():
        ghost.x += 60
        ghost.draw(gm.STAND_R)
    if keys[pygame.K_UP]  and ghost.can_go_up():
        ghost.y -= 60
        ghost.draw(gm.STAND_U)
    if keys[pygame.K_DOWN] and ghost.can_go_down():
        ghost.y += 60
        ghost.draw(gm.STAND_D)
    pygame.display.update()


add_rocks_to_field_list()
set_lvl_1_fields()
ghost = Player(fields[16][8].get_x(), fields[16][8].get_y(), gm.STAND_U)

for i in range(len(yellow_fields)):
    if yellow_fields[i].x == 1310 and yellow_fields[i].y == 620:
        print(True)


while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        redraw_game_window()
pygame.quit()
