import pygame
pygame.init()


class Config:
    def __init__(self):
        """Has settings for global stuff."""
        self.WIN_WIDTH = 800
        self.WIN_HEIGHT = 500
        self.win = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.BALL_COLOR = (3, 252, 215)
        # self.BALL_SIZE = 5