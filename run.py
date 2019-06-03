import pygame
import os
import game_module as gm
from pygame.locals import RESIZABLE
from collections import defaultdict

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
win = pygame.display.set_mode(gm.SIZESCREEN, RESIZABLE)
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

run = True

fields = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
yellow_fields = []
neighbors = defaultdict(list)
visited = []
path = []


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *groups):
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.image = image

    def draw(self, image):
        win.blit(image, (self.x + 7, self.y + 10))

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


class Field(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = gm.ROCK_FIELD

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image


class YellowField(Field):
    def __init__(self, x, y, visible):
        super().__init__(x, y)
        self.visible = visible
        self.image = gm.YELLOW_FIELD

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(super)

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def get_visible(self):
        return self.visible

    def find_neighbors(self, yellow_fields):
        # reversed_list = yellow_fields[::-1]
        for element in yellow_fields:
            if self.x == element.x and self.y - 60 == element.y or self.x == element.x and self.y + 60 == element.y or self.x - 60 == element.x and self.y == element.y or self.x + 60 == element.x and self.y == element.y:
                neighbors[self].append(element)

def draw_final_fields():
    # wyświetlanie fieldow z listy
    for i in range(18):
        for j in range(10):
            win.blit(fields[i][j].get_image(), (fields[i][j].x, fields[i][j].y))


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

    yellow_fields.append(YellowField(fields[0][1].x, fields[0][1].y, True))
    yellow_fields.append(YellowField(fields[1][1].x, fields[1][1].y, True))
    yellow_fields.append(YellowField(fields[2][1].x, fields[2][1].y, True))
    yellow_fields.append(YellowField(fields[3][1].x, fields[3][1].y, True))
    yellow_fields.append(YellowField(fields[3][2].x, fields[3][2].y, True))
    yellow_fields.append(YellowField(fields[3][3].x, fields[3][3].y, True))
    yellow_fields.append(YellowField(fields[3][5].x, fields[3][5].y, True))
    yellow_fields.append(YellowField(fields[3][7].x, fields[3][7].y, True))
    yellow_fields.append(YellowField(fields[4][3].x, fields[4][3].y, True))
    yellow_fields.append(YellowField(fields[4][5].x, fields[4][5].y, True))
    yellow_fields.append(YellowField(fields[4][7].x, fields[4][7].y, True))
    yellow_fields.append(YellowField(fields[4][8].x, fields[4][8].y, True))
    yellow_fields.append(YellowField(fields[5][1].x, fields[5][1].y, True))
    yellow_fields.append(YellowField(fields[5][2].x, fields[5][2].y, True))
    yellow_fields.append(YellowField(fields[5][3].x, fields[5][3].y, True))
    yellow_fields.append(YellowField(fields[5][4].x, fields[5][4].y, True))
    yellow_fields.append(YellowField(fields[5][5].x, fields[5][5].y, True))
    yellow_fields.append(YellowField(fields[5][7].x, fields[5][7].y, True))
    yellow_fields.append(YellowField(fields[6][2].x, fields[6][2].y, True))
    yellow_fields.append(YellowField(fields[6][5].x, fields[6][5].y, True))
    yellow_fields.append(YellowField(fields[6][7].x, fields[6][7].y, True))
    yellow_fields.append(YellowField(fields[7][2].x, fields[7][2].y, True))
    yellow_fields.append(YellowField(fields[7][5].x, fields[7][5].y, True))
    yellow_fields.append(YellowField(fields[7][7].x, fields[7][7].y, True))
    yellow_fields.append(YellowField(fields[8][2].x, fields[8][2].y, True))
    yellow_fields.append(YellowField(fields[8][5].x, fields[8][5].y, True))
    yellow_fields.append(YellowField(fields[8][7].x, fields[8][7].y, True))
    yellow_fields.append(YellowField(fields[8][8].x, fields[8][8].y, True))
    yellow_fields.append(YellowField(fields[9][1].x, fields[9][1].y, True))
    yellow_fields.append(YellowField(fields[9][2].x, fields[9][2].y, True))
    yellow_fields.append(YellowField(fields[9][3].x, fields[9][3].y, True))
    yellow_fields.append(YellowField(fields[9][5].x, fields[9][5].y, True))
    yellow_fields.append(YellowField(fields[9][7].x, fields[9][7].y, True))
    yellow_fields.append(YellowField(fields[10][1].x, fields[10][1].y, True))
    yellow_fields.append(YellowField(fields[10][3].x, fields[10][3].y, True))
    yellow_fields.append(YellowField(fields[10][5].x, fields[10][5].y, True))
    yellow_fields.append(YellowField(fields[10][6].x, fields[10][6].y, True))
    yellow_fields.append(YellowField(fields[10][7].x, fields[10][7].y, True))
    yellow_fields.append(YellowField(fields[11][1].x, fields[11][1].y, True))
    yellow_fields.append(YellowField(fields[12][1].x, fields[12][1].y, True))
    yellow_fields.append(YellowField(fields[12][2].x, fields[12][2].y, True))
    yellow_fields.append(YellowField(fields[12][3].x, fields[12][3].y, True))
    yellow_fields.append(YellowField(fields[12][4].x, fields[12][4].y, True))
    yellow_fields.append(YellowField(fields[12][5].x, fields[12][5].y, True))
    yellow_fields.append(YellowField(fields[12][6].x, fields[12][6].y, True))
    yellow_fields.append(YellowField(fields[13][3].x, fields[13][3].y, True))
    yellow_fields.append(YellowField(fields[13][5].x, fields[13][5].y, True))
    yellow_fields.append(YellowField(fields[14][1].x, fields[14][1].y, True))
    yellow_fields.append(YellowField(fields[14][3].x, fields[14][3].y, True))
    yellow_fields.append(YellowField(fields[14][5].x, fields[14][5].y, True))
    yellow_fields.append(YellowField(fields[15][1].x, fields[15][1].y, True))
    yellow_fields.append(YellowField(fields[15][3].x, fields[15][3].y, True))
    yellow_fields.append(YellowField(fields[15][5].x, fields[15][5].y, True))
    yellow_fields.append(YellowField(fields[15][6].x, fields[15][6].y, True))
    yellow_fields.append(YellowField(fields[16][1].x, fields[16][1].y, True))
    yellow_fields.append(YellowField(fields[16][2].x, fields[16][2].y, True))
    yellow_fields.append(YellowField(fields[16][3].x, fields[16][3].y, True))
    yellow_fields.append(YellowField(fields[16][6].x, fields[16][6].y, True))
    yellow_fields.append(YellowField(fields[16][7].x, fields[16][7].y, True))
    yellow_fields.append(YellowField(fields[16][8].x, fields[16][8].y, True))


def draw_yellow_fields():
    for field in yellow_fields:
        if field.get_visible():
            win.blit(field.get_image(), (field.x, field.y))


def dfs_findpath(start, end):
    _path = []
    return dfs_findpath_(start, end, _path)


def dfs_findpath_(node, end, _path):
    global path
    visited.append(node)
    _path.append(node)

    if node == end:
        path = _path.copy()
        return
    else:
        node_neighbors = neighbors.get(node)
        if node_neighbors is not None:
            for _node in node_neighbors:
                if _node not in visited:
                    dfs_findpath_(_node, end, _path)

    visited.remove(node)
    _path.remove(node)


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
    if keys[pygame.K_UP] and ghost.can_go_up():
        ghost.y -= 60
        ghost.draw(gm.STAND_U)
    if keys[pygame.K_DOWN] and ghost.can_go_down():
        ghost.y += 60
        ghost.draw(gm.STAND_D)
    pygame.display.update()


add_rocks_to_field_list()
set_lvl_1_fields()
ghost = Player(fields[16][8].x, fields[16][8].y, gm.STAND_U)

# finding neighbors
for field in yellow_fields:
    field.find_neighbors(yellow_fields)

for el in yellow_fields:
    print(el.__dict__)

for key, value in neighbors.items():
    print('key{', key.x, ',', key.y, '}')
    for elem in value:
        print('value{', elem.x, ',', elem.y, '}')
start = YellowField(1310, 680, True)
end = YellowField(350, 260, True)
dfs_findpath(start, end)
print(path)

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        redraw_game_window()
pygame.quit()
