import pygame


class Config:
    WIN_WIDTH = 800
    WIN_HEIGHT = 600

    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    BLOCK_LEN = WIN_WIDTH // 10
    BLOCK_THICKNESS = 10

    SPAWN_RECT = pygame.Rect(BLOCK_THICKNESS, BLOCK_THICKNESS, BLOCK_LEN - 2 * BLOCK_THICKNESS, BLOCK_LEN - 2 * BLOCK_THICKNESS)
    BALL_SPAWN_POS = list(SPAWN_RECT.center)

    FPS = 60
    clock = pygame.time.Clock()

    TILE_COLOR = (241, 245, 140)
    BG_COLOR = (0, 0, 0)
    BALL_COLOR = (14, 235, 220)
