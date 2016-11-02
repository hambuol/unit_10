import pygame, sys
from pygame.locals import *
import bricks

numberofB = 9
SPACE = 5

pygame.init()
mainSurface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bricks")



width = (500 - ((numberofB + 1) * SPACE))/numberofB
brick = bricks.Brick(mainSurface, width)



brick.drawbrick(SPACE, 470)
brick.drawbrick(SPACE + 55, 470)
brick.drawbrick(SPACE + 110, 470)
brick.drawbrick(SPACE + 165, 470)






while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()