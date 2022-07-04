import pygame


class BouncyBall:
    def __init__(self, settings, ball_properties):
        """Has physics and code for one single bouncy ball."""
        self.settings = settings
        self.x_vel = ball_properties["x_vel"]
        self.y_vel = ball_properties["y_vel"]
        self.pos = ball_properties["pos"].copy()

        self.img = pygame.image.load("assets/ball2.png")
        self.mask = pygame.mask.from_surface(self.img)

        self.rect = self.img.get_rect()
        self.RADIUS = self.rect.width / 2

    def draw(self):
        """Draws the ball on the surface."""
        self.settings.win.blit(self.img, self.pos)

    def collision(self, collision_pos):
        """Changes direction due to collision."""
        # y axis collision
        if collision_pos[1] >= self.pos[1] or collision_pos[1] <= self.pos[1] + 2 * self.RADIUS:
            self.y_vel *= -1

    def move(self):
        """Moves the ball."""
        self.pos[0] += self.x_vel / self.settings.FPS
        self.pos[1] += self.y_vel / self.settings.FPS

    def __str__(self):
        return f"{self.x_vel}{self.y_vel}"