import pygame


class BouncyBall:
    def __init__(self, settings, ball_properties):
        """Has physics and code for one single bouncy ball."""
        self.settings = settings
        self.x_vel = ball_properties["x_vel"]
        self.y_vel = ball_properties["y_vel"]
        self.pos = ball_properties["pos"].copy()

    def draw(self):
        """Draws the ball on the surface."""
        pygame.draw.circle(
            self.settings.win,
            self.settings.BALL_COLOR,
            self.pos,
            self.settings.BALL_SIZE
        )

    def move(self):
        """Moves the ball and and calls the check collision."""
        self.pos[0] += self.x_vel / self.settings.FPS
        self.pos[1] += self.y_vel / self.settings.FPS

    def __str__(self):
        return f"{self.x_vel}{self.y_vel}"