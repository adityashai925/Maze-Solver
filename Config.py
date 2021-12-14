import pygame


class Config:
    WIN_WIDTH = 500
    WIN_HEIGHT = 500

    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    FPS = 60
    clock = pygame.time.Clock()

    TILE_COLOR = (255, 0, 0)
    BG_COLOR = (0, 0, 0)
    BALL_COLOR = (255, 255, 255)