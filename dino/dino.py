import pygame, sys, random
from pygame.locals import *

class Dino:
    def __init__(self):
        self.x = 20
        self.y = 200
        # self.dx = 0
        self.dy = 0
        self.leg_flag = 0
        self.time = 0
        self.dino_Img = pygame.image.load('dino1a1.png')
        self.rect = self.dino_Img.get_rect()
        self.jumping = False
    
    def onTheGround(self):
        if self.y >= 200:
            return True
        else:
            return False
    
    def onTheTop(self):
        if self.y <= 100:
            return True
        else:
            return False

    # def moveRight(self):
    #     self.dx = 180

    # def moveLeft(self):
    #     self.dx = -180

    def jump(self):
        if self.onTheGround():
            self.dy -= 300
            self.jumping = True

    def update(self, deltatime):
        if self.onTheTop():
            self.dy += 50
            self.jumping = False
 
        if self.onTheGround() and not self.jumping:
            self.dy = 0
            self.y = 200

        self.time += 1
        if self.time == 6:
            if self.leg_flag == 0:
                self.leg_flag = 1
                self.dino_Img = pygame.image.load('dino1b1.png')
            else:
                self.dino_Img = pygame.image.load('dino1a1.png')
                self.leg_flag = 0
            self.time = 0

        # self.x += self.dx * deltatime
        self.y += self.dy * deltatime
        self.rect.topleft = self.x, self.y

class Counter:
    def __init__(self):
        pygame.font.init()
        self.BLACK = (0, 0, 0)
        self.myfont = pygame.font.SysFont("monospace", 20)
        self.count = 0
        text = str(self.count).zfill(5)
        self.counterText = self.myfont.render(text, 1, self.BLACK)
        self.check = 0
        
    def update(self):
        self.check += 1
        if self.check == 6:
            self.count += 1
            self.check = 0
        text = str(self.count).zfill(5)
        self.counterText = self.myfont.render(text, 1, self.BLACK)
 
class Game:
    def __init__(self):
        self._running = True
        self.dino = Dino()
        self.background = Background()
        self.counter = Counter()
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        self.cactuses = pygame.sprite.Group()
        self.respawn = 100        

        pygame.init()

        self._display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption('Dinozaur')

        self.GRAY = (248, 248, 248)
        self.WHITE = (255, 255, 255)

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def execute(self):
        deltatime = 0
        RED = (255, 0, 0)
        self.fpsClock.tick(self.FPS)
 
        while( self._running ):
            keys = pygame.key.get_pressed()
 
            # if (keys[K_RIGHT]):
            #     self.dino.moveRight()
 
            # if (keys[K_LEFT]):
            #     self.dino.moveLeft()
 
            if (keys[K_SPACE]):
                self.dino.jump()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            for event in pygame.event.get():
                self.on_event(event)
 
            self._display_surface.fill(self.GRAY)
            self._display_surface.blit(self.background.backgroundImg[self.background.random1],(self.background.x,self.background.y))
            self._display_surface.blit(self.background.backgroundImg[self.background.random2],(self.background.x2,self.background.y))
            self._display_surface.blit(self.dino.dino_Img,(self.dino.x,self.dino.y))
            self._display_surface.blit(self.counter.counterText, (730, 10))
            self.counter.update()
            self.background.update()
 
            self.dino.update(deltatime)
            self.respawn -= 1
            if self.respawn == 0:
                self.cactuses.add(Cactus())
                self.respawn = random.randint(60, 200)
 
            for cactus in self.cactuses:
                is_collided = pygame.sprite.collide_rect(self.dino, cactus)
                if (is_collided):
                    #print("K A B U M !!!")
                    myfont = pygame.font.SysFont("arial", 30)
                    label = myfont.render("K A B U M !!!", 1, RED)
                    self._display_surface.blit(label, (100, 100))
 
            self.cactuses.update()
            self.cactuses.draw(self._display_surface)
            
            pygame.display.update()
 
            deltatime = self.fpsClock.tick(self.FPS)/1000.0

class Background():
    def __init__(self):
        self.backgroundImg = []
        self.backgroundImg.append(pygame.image.load('teren.png'))
        self.backgroundImg.append(pygame.image.load('teren2.png'))
        self.backgroundImg.append(pygame.image.load('teren3.png'))
        self.rectBg = self.backgroundImg[0].get_rect()
        self.width = self.rectBg.width
        self.x = 0
        self.x2 = self.width
        self.y = 240
        self.dx = -10
        self.random1 = 0
        self.random2 = 1
    
    def update(self):
        self.x += self.dx
        if self.x <= -self.width:
            self.x = self.width
            self.random1 = random.randint(0,2)
        self.x2 += self.dx
        if self.x2 <= -self.width:
            self.x2 = self.width
            self.random2 = random.randint(0,2)

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cactusImg = []
        cactusImg.append(pygame.image.load('kaktus1.png'))
        cactusImg.append(pygame.image.load('kaktus2.png'))
        cactusImg.append(pygame.image.load('kaktus3.png'))
        cactusImg.append(pygame.image.load('kaktus4.png'))
        rand = random.randint(0,3)
        self.image = cactusImg[rand]
        self.rect = self.image.get_rect()
        self.x = 800
        if (rand == 2):
            self.y = 218
        else:
            self.y = 200
        self.rect.move_ip(self.x, self.y)
        self.dx = -10

    def update(self):
        self.rect = self.rect.move(self.dx, 0)

if __name__ == "__main__" :
    runGame = Game()
    runGame.execute()