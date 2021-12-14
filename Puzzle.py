import pygame
pygame.init()

from Config import Config


class Puzzle:
    def __init__(self):
        """
        Has the rect for tiles.
        """
        self.TILES = [
            pygame.Rect(200, 50, 200, 50),
            pygame.Rect(200, 300, 200, 50),
            pygame.Rect(200, 50, 50, 300),
            pygame.Rect(350, 50, 50, 300),
        ]

    def draw_puzzle(self):
        """
        Draws the puzzle on the Config.WIN
        """
        Config.WIN.fill(Config.BG_COLOR)

        for tile in self.TILES:
            pygame.draw.rect(Config.WIN, Config.TILE_COLOR, tile)