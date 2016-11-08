# written by oliver hamburger
# program is a class for creating a brick pyramid
# last modified 11/8/16


# imports needed moduel pygame
import pygame


class Brick:
    """class that sets basics needed to make a brick pyramid. user can draw a brick"""
    def __init__(self, mainsurface, width):
        self.mainsurface = mainsurface
        self.width = width
        pygame.init()

    def drawbrick(self, x, y, r, g, b):
        """

        :param x: x position of brick
        :param y: y position of brick
        :param r: ammount of red color in a brick
        :param g: ammount of green color in a brick
        :param b: ammount of blue color in a brick
        :return: none
        """
        pygame.draw.rect(self.mainsurface, (r, g, b), (x, y, self.width, 25), 0)
        pygame.display.update()
