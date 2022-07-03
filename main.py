import math

import pygame
pygame.init()

from Config import Config
from BouncyBall import BouncyBall


class Main:
    def __init__(self):
        """Has global functions and variables."""
        self.Settings = Config()

    def generate_balls(self):
        """Generates list containing BouncyBall objects"""
        self.balls = []
        magnitude = 200
        pos = [self.Settings.WIN_WIDTH // 2, self.Settings.WIN_HEIGHT // 2]

        for angle in range(0, 360):
            angle = math.radians(angle)
            x_vel = magnitude * math.cos(angle)
            y_vel = magnitude * math.sin(angle)

            ball_properties = {
                "pos": pos,
                "x_vel": x_vel,
                "y_vel": y_vel,
                # "angle": math.degrees(angle)
            }

            Ball = BouncyBall(self.Settings, ball_properties)
            self.balls.append(Ball)

    def draw(self):
        """Draws the maze and the balls."""
        self.Settings.win.fill((0, 0, 0))

        for ball in self.balls:
            ball.draw()

    def main(self):
        """Main loop."""
        self.generate_balls()
 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            for ball in self.balls:
                ball.move()
                # print(ball)

            self.draw()
            pygame.display.update()
            self.Settings.clock.tick(self.Settings.FPS)


if __name__ == "__main__":
    Code = Main()
    Code.main()