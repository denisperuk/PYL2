from functions import *
from mini_game import *


width = 640
height = 480
display = (width, height)
k = 1

pygame.init()
screen = pygame.display.set_mode(display)
pygame.display.set_caption("mario")
ground = pygame.Surface((width, height))
ground.fill(pygame.Color(5))
timer = pygame.time.Clock()
entities = pygame.sprite.Group()
hero = Player(224, 32)
mush = Monster(300, 32, 3, 0, 91, 91)
left = False
right = False
up = False
generate_level(load_level('map.txt'))
entities.add(hero)
while pygame.event.wait().type != pygame.QUIT and k == 1:
    timer.tick(60)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            k = 0
            break
        elif event.type == KEYDOWN and event.key == K_LEFT:
            left = True
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            right = True
        elif event.type == KEYUP and event.key == K_RIGHT:
            right = False
        elif event.type == KEYUP and event.key == K_LEFT:
            left = False
        elif event.type == KEYDOWN and event.key == K_UP:
            up = True
        elif event.type == KEYUP and event.key == K_UP:
            up = False
        elif pygame.key.get_pressed()[pygame.K_SPACE]:
            secret()
            camera = Camera()
            camera.update(hero)
        hero.update(left, right, up)
    screen.blit(ground, (0, 0))
    pygame.display.update()
pygame.quit()