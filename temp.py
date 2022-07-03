Settings = Config()
number_of_balls = 1
balls = []

for ball_num in range(number_of_balls):
    ball_properties = {
        "x_vel": 1000,
        "y_vel": -1000,
        "pos": [50, 450],
    }
    Ball = BouncyBall(Settings, ball_properties)
    balls.append(Ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    Settings.win.fill((0, 0, 0))

    for ball in balls:
        ball.move()
        ball.draw()

    pygame.display.update()
    Settings.clock.tick(Settings.FPS)