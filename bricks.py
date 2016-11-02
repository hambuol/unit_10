import pygame

class Brick:
    def __init__(self, mainsurface, width):
        self.mainsurface = mainsurface
        self.width = width
        pygame.init()

    def drawbrick(self, x, y):
        pygame.draw.rect(self.mainsurface, (255, 0, 0), (x, y, self.width,25), 0)
        pygame.display.update()

