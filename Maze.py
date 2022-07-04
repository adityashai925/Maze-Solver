import pygame
pygame.init()


class Maze:
    def __init__(self):
        """Handles maze related methods and attributes."""
        self.img = pygame.image.load("assets/maze.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.img)