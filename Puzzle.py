import pygame
pygame.init()

from Config import Config


class Puzzle:
    def __init__(self):
        """
        Has the rect for tiles.
        """
        self.TILES = [
            pygame.Rect(0, -25, Config.WIN_WIDTH, 25),
            pygame.Rect(0, Config.WIN_HEIGHT, Config.WIN_WIDTH, 25),
            pygame.Rect(-25, 0, 25, Config.WIN_HEIGHT),
            pygame.Rect(Config.WIN_WIDTH, 0, 25, Config.WIN_HEIGHT),
            pygame.Rect(0, 0, Config.BLOCK_LEN, Config.BLOCK_THICKNESS),
            pygame.Rect(Config.BLOCK_LEN - Config.BLOCK_THICKNESS, 0, Config.BLOCK_THICKNESS, Config.BLOCK_LEN),
            pygame.Rect(Config.BLOCK_LEN - Config.BLOCK_THICKNESS, Config.BLOCK_LEN - Config.BLOCK_THICKNESS, Config.WIN_WIDTH - Config.BLOCK_LEN + Config.BLOCK_THICKNESS, Config.BLOCK_THICKNESS),
        ]

    def draw_puzzle(self):
        """
        Draws the puzzle on the Config.WIN
        """
        Config.WIN.fill(Config.BG_COLOR)

        for tile in self.TILES:
            pygame.draw.rect(Config.WIN, Config.TILE_COLOR, tile)