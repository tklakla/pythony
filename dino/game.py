import pygame, sys
from pygame.locals import *
 
pygame.init()

FPS = 60 
fpsClock = pygame.time.Clock()

DISPLAY_SURFACE = pygame.display.set_mode((1500, 100))
pygame.display.set_caption('Dinozaur!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (225, 225, 225)

dino_Img = pygame.image.load('dino3.png')
dino_x = 10
dino_y = 10
direction = 'right'
dino_jump = False
dino_fall = False

while True: 
    DISPLAY_SURFACE.fill(WHITE)

    # if direction == 'right':
    #     dino_x += 4
    #     if dino_x == 482:
    #         dino_Img = pygame.transform.flip(dino_Img, True, False)
    #         direction = 'left'
    # elif direction == 'left':
    #     dino_x -= 4
    #     if dino_x == 22:
    #         dino_Img = pygame.transform.flip(dino_Img, True, False)
    #         direction = 'right'
    
    if dino_jump == True:
        if dino_y > 2:
            dino_y = dino_y - 2
        else:
            dino_fall = True
            dino_jump = False
 
    elif dino_fall == True:
        if dino_y < 10:
            dino_y = dino_y + 2
        else:
            dino_fall = False
 
    else:
        if direction == 'right':
            dino_x += 4
            if dino_x == 1430:
                dino_Img = pygame.transform.flip(dino_Img, True, False)
                direction = 'left'
        elif direction == 'left':
            dino_x -= 4
            if dino_x == 22:
                dino_Img = pygame.transform.flip(dino_Img, True, False)
                direction = 'right'
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == KEYUP and event.key == K_SPACE):
            dino_jump = True

    DISPLAY_SURFACE.blit(dino_Img, (dino_x, dino_y))

#while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

    #DISPLAY_SURFACE.fill(WHITE)
    #pygame.draw.line(DISPLAY_SURFACE, BLACK, (60, 60), (120, 60), 4)
    #pygame.draw.line(DISPLAY_SURFACE, GRAY, (60, 70), (120, 70), 4)
    #pygame.draw.circle(DISPLAY_SURFACE, GRAY, (300, 50), 20, 0)
    #pygame.draw.rect(DISPLAY_SURFACE, GREEN, (200, 150, 100, 50))

    #myfont = pygame.font.SysFont("monospace", 30)
    #label = myfont.render("Hello World!", 1, BLACK)
    #DISPLAY_SURFACE.blit(label, (100, 100))

    
