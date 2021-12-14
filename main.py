import pygame
pygame.init()

from Puzzle import Puzzle
from Config import Config
from BouncyBall import BouncyBall


PuzzleObj = Puzzle()
Ball1 = BouncyBall([300, 150], -0.5, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    PuzzleObj.draw_puzzle()
    Ball1.move(PuzzleObj.TILES)
    Ball1.draw()
    pygame.display.update()
    Config.clock.tick(Config.FPS)
