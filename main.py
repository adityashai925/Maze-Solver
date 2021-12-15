import pygame
pygame.init()
import random

from Puzzle import Puzzle
from Config import Config
from BouncyBall import BouncyBall


PuzzleObj = Puzzle()
balls = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if len(balls) != 2000:
        x_vel = random.randint(-350, 350) / 100
        y_vel = random.randint(-350, 350) / 100

        if x_vel != 0 and y_vel != 0:
            balls.append(BouncyBall(Config.BALL_SPAWN_POS, x_vel, y_vel))

    PuzzleObj.draw_puzzle()

    for ball in balls:
        ball.move(PuzzleObj.TILES)
        ball.draw()

    pygame.display.update()
    Config.clock.tick(Config.FPS)
