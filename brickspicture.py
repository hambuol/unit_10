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

xpos = SPACE
for x in range(numberofB):
    brick.drawbrick(xpos, 470, 255, 0, 0)
    xpos += width + SPACE

xpos = SPACE + width + 5
for x in range(numberofB - 2):
    brick.drawbrick(xpos, 440, 200, 125, 40)
    xpos += width + SPACE

xpos = SPACE + width * 2 + 10
for x in range(numberofB - 4):
    brick.drawbrick(xpos, 410, 75, 50, 70)
    xpos += width + SPACE

xpos = SPACE + width * 3 + 15
for x in range(numberofB - 6):
    brick.drawbrick(xpos, 380, 75, 120, 120)
    xpos += width + SPACE

xpos = SPACE + width * 4 + 20
for x in range(numberofB - 8):
    brick.drawbrick(xpos, 350, 0, 255, 0)
    xpos += width + SPACE

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
