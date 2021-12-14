import pygame

from Config import Config


class BouncyBall:
    def __init__(self, pos, x_vel, y_vel):
        """
        Has attrs for only one bouncy ball.
        """
        self.SIZE = 4
        self.pos = pos
        self.x_vel = x_vel
        self.y_vel = y_vel

    def check_collision(self, tiles):
        """
        Checks if the ball is colliding with a tile.
        """
        self.top_y = self.pos[1] - self.SIZE
        self.bottom_y = self.pos[1] + self.SIZE
        self.left_x = self.pos[0] - self.SIZE
        self.right_x = self.pos[0] + self.SIZE

        for tile in tiles:
            # for collision of bottom of ball with top of the tile
            if (self.bottom_y >= tile.y and self.bottom_y <= tile.y + tile.height and self.top_y < tile.y and ((self.left_x >= tile.x and self.left_x <= tile.x + tile.width) or (self.right_x >= tile.x and self.right_x <= tile.x + tile.width))):
                self.y_vel = -1 * self.y_vel

            # elif self.pos[1] <= tile.y + tile.height:
            #     self.y_vel = -1 * self.y_vel

    def move(self, tiles):
        """
        Updates x and y values using x_vel and y_vel.
        """
        self.check_collision(tiles)

        self.pos[0] += self.x_vel
        self.pos[1] += self.y_vel

    def draw(self):
        """
        Draws the single ball.
        """
        pygame.draw.circle(Config.WIN, Config.BALL_COLOR, self.pos, self.SIZE)