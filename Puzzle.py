import pygame
pygame.init()

from Config import Config


class Puzzle:
    def __init__(self):
        """
        Has the rect for tiles.
        """
        self.TILES = [
            pygame.Rect(0, 0, Config.WIN_WIDTH, Config.BLOCK_THICKNESS),
            pygame.Rect(0, Config.WIN_HEIGHT - Config.BLOCK_THICKNESS, Config.WIN_WIDTH, Config.BLOCK_THICKNESS),
            pygame.Rect(0, 0, Config.BLOCK_THICKNESS, Config.WIN_HEIGHT),
            pygame.Rect(Config.WIN_WIDTH - Config.BLOCK_THICKNESS, 0, Config.BLOCK_THICKNESS, Config.WIN_HEIGHT),
            pygame.Rect(Config.BLOCK_LEN - Config.BLOCK_THICKNESS, 0, Config.BLOCK_THICKNESS, Config.BLOCK_LEN),
            pygame.Rect(Config.BLOCK_LEN - Config.BLOCK_THICKNESS, Config.BLOCK_LEN - Config.BLOCK_THICKNESS, Config.WIN_WIDTH - Config.BLOCK_LEN, Config.BLOCK_THICKNESS),
            pygame.Rect(Config.WIN_WIDTH - Config.BLOCK_LEN, Config.WIN_HEIGHT - Config.BLOCK_LEN, Config.BLOCK_THICKNESS, Config.BLOCK_LEN),
            pygame.Rect(0, Config.WIN_HEIGHT - Config.BLOCK_LEN, Config.WIN_WIDTH - Config.BLOCK_LEN, Config.BLOCK_THICKNESS),
            pygame.Rect(Config.BLOCK_THICKNESS, 5 * Config.BLOCK_LEN, Config.BLOCK_LEN, Config.BLOCK_THICKNESS),
            pygame.Rect(4 * Config.BLOCK_LEN, Config.BLOCK_LEN - Config.BLOCK_THICKNESS, Config.BLOCK_THICKNESS, 2 * Config.BLOCK_LEN),
            pygame.Rect(Config.BLOCK_LEN - Config.BLOCK_THICKNESS, 3 * Config.BLOCK_LEN - Config.BLOCK_THICKNESS, 5 * Config.BLOCK_LEN, Config.BLOCK_THICKNESS),
            pygame.Rect(Config.BLOCK_LEN - Config.BLOCK_THICKNESS, 2 * Config.BLOCK_LEN- Config.BLOCK_THICKNESS, Config.BLOCK_LEN, Config.BLOCK_THICKNESS),
            pygame.Rect(Config.BLOCK_LEN - Config.BLOCK_THICKNESS, 2 * Config.BLOCK_LEN- Config.BLOCK_THICKNESS, Config.BLOCK_THICKNESS, Config.BLOCK_LEN),
        ]

    def draw_puzzle(self):
        """
        Draws the puzzle on the Config.WIN
        """
        Config.WIN.fill(Config.BG_COLOR)

        for tile in self.TILES:
            pygame.draw.rect(Config.WIN, Config.TILE_COLOR, tile)