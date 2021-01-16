from pygame import *
import sys
import os
import pygame
block_w = 32
block_h = 32
entities = pygame.sprite.Group()
block_group = pygame.sprite.Group()
platform = []
ms = 7
w = 22
h = 32
jump = 3
gravity = 0.35


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startY = y
        self.startX = x
        self.yvel = 0
        self.onGround = False
        self.image = Surface((w, h))
        self.image = image.load("models\mario2.png")
        self.image4 = image.load("models\mario4.png")
        self.image2 = image.load("models\mario3.png")
        self.image1 = image.load("models\mario.png")
        self.rect = Rect(x, y, w, h)

    def update(self, left, right, up):
        if left:
            self.xvel = -ms
            self.change_anim(self.image, self.image1, self.image4)

        if right:
            self.xvel = ms
            self.change_anim(self.image4, self.image1, self.image)

        if up:
            if self.onGround:
                self.yvel = -jump
                self.onGround = False
                self.rect.y += self.yvel
                self.change_anim(self.image, self.image2, self.image)
            if not self.onGround:
                self.yvel += gravity

        if not (left or right):
            self.xvel = 0

        self.rect.x += self.xvel

    def change_anim(self, img1, img2, img3):
        self.frames = [img1, img2, img3]
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def collide(self, xvel, yvel):
        for p in platform:
            if sprite.collide_rect(self, p):
                if isinstance(p, Monster):
                       self.die()
                else:
                    if xvel > 0:
                        self.rect.right = p.rect.left

                    if xvel < 0:
                        self.rect.left = p.rect.right

                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0

                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0

    def die(self):
        self.onGround = False
        self.image = Surface((w, h))
        self.image = image.load("models\mario4.png")
        self.rect = Rect(self.startX, self.startY, w, h)


def load_image(filename, colorkey=None, name='', n_scale=None, flip=False):
    fullname = os.path.join("models", name, filename)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    if n_scale is not None:
        image = transform.scale(image, (image.get_size()[0] // n_scale, image.get_size()[1] // n_scale))
    if flip is not False:
        image = transform.flip(image, True, False)
    return image

def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


block_im = {
    'sky': load_image('sky.png', name='map'),
    'earth': load_image('earth.png', name='map'),
    'Pipe3': load_image('Pipe3.png', name='map'),
    'Pipe2': load_image('Pipe2.png', name='map'),
    'water_up': load_image('water_up.png', name='map'),
    'void': load_image('void.png', name='map'),
    'Pipe4': load_image('Pipe4.png', name='map'),
    'Pipe1': load_image('Pipe1.png', name='map'),
    'water_down': load_image('water_down.png', name='map'),
    'hill': load_image('hill.png', name='map'),
    'hill2': load_image('hill2.png', name='map'),
    'hill3': load_image('hill3.png', name='map'),
    'hill4': load_image('hill4.png', name='map'),
    'hill56': load_image('hill56.png', name='map'),
    'hill7': load_image('hill7.png', name='map'),
    'hill8': load_image('hill8.png', name='map'),
    'hill9': load_image('hill9.png', name='map'),
    'coinblock': load_image('coinblock.png', name='map'),
    'castleg1': load_image('castleg1.png', name='map'),
    'castleg4': load_image('castleg4.png', name='map'),
    'castleg3': load_image('castleg3.png', name='map'),
    'castleg2': load_image('castleg2.png', name='map'),
    'simpblock': load_image('simpblock.png', name='map'),
    'brics2': load_image('brics2.png', name='map'),
    'bricks': load_image('bricks.png', name='map'),
    'stick': load_image('stick.png', name='map'),
    'flag': load_image('flag.png', name='map'),
}

class Block(sprite.Sprite):
    def __init__(self, block_type, x, y):
        super().__init__(block_group, entities)
        self.image = block_im[block_type]
        self.rect = self.image.get_rect().move(
            block_w * x, block_h * y)



def generate_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Block('sky', x, y)
            elif level[y][x] == '@':
                platform.append(Block('simpblock', x, y))
            elif level[y][x] == 'E':
                platform.append(Block('earth', x, y))
            elif level[y][x] == 'P':
                platform.append(Block('Pipe3', x, y))
            elif level[y][x] == 'p':
                platform.append(Block('Pipe4', x, y))
            elif level[y][x] == 'T':
                platform.append(Block('Pipe1', x, y))
            elif level[y][x] == 't':
                platform.append(Block('Pipe2', x, y))
            elif level[y][x] == '1':
                Block('hill', x, y)
            elif level[y][x] == 'X':
                Block('stick', x, y)
            elif level[y][x] == '<':
                Block('flag', x, y)
            elif level[y][x] == '8':
                Block('hill8', x, y)
            elif level[y][x] == '2':
                Block('hill2', x, y)
            elif level[y][x] == '3':
                Block('hill3', x, y)
            elif level[y][x] == '4':
                Block('hill4', x, y)
            elif level[y][x] == '5':
                Block('hill56', x, y)
            elif level[y][x] == '7':
                Block('hill7', x, y)
            elif level[y][x] == 'B':
                platform.append(Block('bricks', x, y))
            elif level[y][x] == 'A':
                platform.append(Block('brics2', x, y))
            elif level[y][x] == '9':
                Block('hill9', x, y)
            elif level[y][x] == 'C':
                Block('castleg1', x, y)
            elif level[y][x] == 'c':
                Block('castleg2', x, y)
            elif level[y][x] == 'K':
                Block('castleg3', x, y)
            elif level[y][x] == 'U':
                Block('castleg4', x, y)
            elif level[y][x] == 'V':
                Block('void', x, y)
            elif level[y][x] == '?':
                platform.append(Block("coinblock", x, y))

mw = 32
mh = 32


class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, maxleft, maxup):
        sprite.Sprite.__init__(self)
        self.image = Surface((mw, mh))
        self.rect = Rect(x, y, mw, mh)
        self.startx = x
        self.starty = y
        self.maxleft = maxleft
        self.maxup = maxup
        self.xvel = left

    def change_anim(self, img1, img2, img3):
        self.frames = [img1, img2, img3]
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def update(self):
        self.rect.y += self.yvel
        self.rect.x += self.xvel
        self.image1 = load_image("models/monsters/Mush1.png")
        self.image2 = load_image("models/monsters/Mush2.png")
        if (abs(self.startx - self.rect.x) > self.maxleft):
            self.change_anim(self.image1, self.image2, self.image1)
            self.xvel = -self.xvel
        if (abs(self.starty - self.rect.y) > self.maxup):
            self.change_anim(self.image2, self.image1, self.image2)
            self.yvel = -self.yvel


    def collide(self, ):
        for p in platform:
            if sprite.collide_rect(self, p) and self != p:
                self.xvel = - self.xvel
                self.yvel = - self.yvel



class Camera:
    def __init__(self):
        self.dx = 0

    def apply(self, obj):
        obj.rect.x += self.dx

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - w // 2)