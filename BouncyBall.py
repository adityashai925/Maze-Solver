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
            tile_top = tile.y
            tile_bottom = tile.y + tile.height
            tile_left = tile.x
            tile_right = tile.x + tile.width

            lower_edge_is_intersecting = self.bottom_y >= tile_top and self.bottom_y < tile_bottom
            upper_edge_is_intersecting = self.top_y <= tile_bottom and self.top_y > tile_top
            left_edge_is_intersecting = self.left_x <= tile_right and self.left_x >= tile_left
            right_edge_is_intersecting = self.right_x >= tile_left and self.right_x <= tile_right

            lower_edge_is_colliding = lower_edge_is_intersecting and (left_edge_is_intersecting or right_edge_is_intersecting) and not upper_edge_is_intersecting
            upper_edge_is_colliding = upper_edge_is_intersecting and (left_edge_is_intersecting or right_edge_is_intersecting) and not lower_edge_is_intersecting
            left_edge_is_colliding = left_edge_is_intersecting and (lower_edge_is_intersecting or upper_edge_is_intersecting) and not right_edge_is_intersecting
            right_edge_is_colliding = right_edge_is_intersecting and (lower_edge_is_intersecting or upper_edge_is_intersecting) and not left_edge_is_intersecting

            # collision check on y axis
            if lower_edge_is_colliding or upper_edge_is_colliding:
                self.y_vel *= -1

            # collision check on x axis
            if left_edge_is_colliding or right_edge_is_colliding:
                self.x_vel *= -1

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