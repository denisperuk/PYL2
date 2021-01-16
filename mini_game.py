import pygame
import random
explosion = [pygame.image.load("Explosion_001.png"),
pygame.image.load("Explosion_002.png"),
pygame.image.load("Explosion_003.png"),
pygame.image.load("Explosion_004.png"),
pygame.image.load("Explosion_005.png"),
pygame.image.load("Explosion_006.png"),
pygame.image.load("Explosion_007.png"),
pygame.image.load("Explosion_008.png")]
font_name = pygame.font.match_font("arial")


def secret():

    def draw_text(win,text,size,x,y):
        font = pygame.font.Font(font_name,size)
        text_surface = font.render(text,True,(0,255,0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        win.blit(text_surface,text_rect)
    class Explosion:
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.expl = 0
        def draw(self,win):
            win.blit(explosion[self.expl],(self.x,self.y))
    class Stars:
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.v = 1
        def draw(self,win):
            pygame.draw.circle(win,(255,255,255),(self.x,self.y),0,0)
    class Classs:
        def __init__(self,x):
            self.x = x + 50
            self.y = 300
            self.v = 10
        def draww(self,win):
            pygame.draw.line(win,(0,100,255),(self.x,self.y),(self.x,self.y + 10),3)
    class Win:
        def __init__(self,x):
            self.x = x
            self.y = 0
            self.v = 5
        def draw(self,win):
            win.blit(enemy,(self.x,self.y))
    pygame.init()
    run = True
    x = 250
    y = 0
    sk = 0
    sv = 0
    sc = 2
    an = 0
    score = 0
    scr = pygame.display.set_mode((500,381))
    pygame.display.set_caption("игра")
    color = (255,255,0)
    stars = []
    expll = []
    enemy = pygame.image.load("enemy3.png")
    ship = pygame.image.load("player.png")
    bg = pygame.image.load("saturn.jpg")

    for i in range(100):
        xs = random.randint(0,381)
        ys = random.randint(0,381)
        stars.append(Stars(xs,ys))
    sn = []
    List = []
    while run:
        scr.blit(bg,(0,0))
        xs = random.randint(0,381)
        a = random.randint(0,381)
        if sk == 10:
            stars.append(Stars(xs,0))
            sk = 0
        else:
            sk += 1
        if an == 30:
            List.append(Win(a))
            an = 0
        else:
            an += 1
        for star in stars:
            if star.y <= 381:
                star.draw(scr)
                star.y += star.v
            else:
                stars.pop(stars.index(star))
        for anv in List:
            if anv.y <= 381:
                anv.draw(scr)
                anv.y += anv.v
            else:
                List.pop(List.index(anv))
                score -= 100
        pygame.time.delay(30)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if sc >= 2:
                if sv < 10:
                    sn.append(Classs(x))
                    score -= 10
                    sv += 1
                    sc = 0
                else:
                    sv = 0
            else:
                sc +=1
        for snaryad in sn:
            if snaryad.y > 0:
                snaryad.draww(scr)
                snaryad.y -= snaryad.v
            else:
                sn.pop(sn.index(snaryad))
        if keys[pygame.K_LEFT]and x >= 0:
            x -= 10
        if keys[pygame.K_RIGHT] and x <= 381:
            x += 10
        scr.blit(ship,(x,300))
        for j in sn:
            for i in List:
                if j.x >= i.x and j.x <= i.x + 75 and j.y >= i.y - 30 and j.y <= i.y + 30:
                    expll.append(Explosion(i.x - 20, i.y -20))
                    List.pop(List.index(i))
                    sn.pop(sn.index(j))
                    score += 100
        for h in expll:
            if h.expl < 8:
                h.draw(scr)
                h.expl += 1
            else:
                expll.pop(expll.index(h))
        draw_text(scr,"score:" + str(score),18,250,10)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
