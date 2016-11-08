# written by oliver hamburger
# program draws a brick pyramid in pygame
# last modified 11/8/16


# imports needed moduel pygame
import pygame, sys
from pygame.locals import *
# imports bricks class
import bricks
# sets backround color to white
backround_c = (255, 255, 255)
# sets number of brick in row in pyramid
numberofB = 9
SPACE_BETWEEN_BRICKS = 5

pygame.init()
# made variable to pass width of screen size
W = 650
# creates surface in pygame, sets caption, and fills the screen color
mainSurface = pygame.display.set_mode((W, 500))
pygame.display.set_caption("Bricks")
mainSurface.fill(backround_c)

# calculates the width of the brick pyramid
width = (W - ((numberofB + 1) * SPACE_BETWEEN_BRICKS))/numberofB
brick = bricks.Brick(mainSurface, width)
# sets red green and blue for brick color to a set ammount
r = 255
g = 10
b = 12
# starting y position
ypos = 470
# starting x position
xpos = SPACE_BETWEEN_BRICKS
# height of brick
height = 25
# loop that updated the number of brick, x-y position and color for each row of bricks
for q in range(5):
    # loop that creates a row of bricks
    for x in range(numberofB):
        brick.drawbrick(xpos, ypos, r, g, b)
        xpos += width + SPACE_BETWEEN_BRICKS
    ypos -= height + SPACE_BETWEEN_BRICKS
    xpos = (SPACE_BETWEEN_BRICKS + width) * q + SPACE_BETWEEN_BRICKS + SPACE_BETWEEN_BRICKS + width
    numberofB -= 2
    r = 60 * q
    g = 80 * q
    b = 80 * q
# loop that runs pygame untill it is exited out by user
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
