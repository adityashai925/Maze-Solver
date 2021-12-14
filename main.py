import pygame
pygame.init()
import random

from Puzzle import Puzzle
from Config import Config
from BouncyBall import BouncyBall


PuzzleObj = Puzzle()
balls = []
for _ in range(100):
    x_vel = random.randint(-500, 500) / 100
    y_vel = random.randint(-500, 500) / 100

    if x_vel != 0 and y_vel != 0:
        balls.append(BouncyBall([300, 150], x_vel, y_vel))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    PuzzleObj.draw_puzzle()

    for ball in balls:
        ball.move(PuzzleObj.TILES)
        ball.draw()

    pygame.display.update()
    Config.clock.tick(Config.FPS)
