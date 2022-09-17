from pygame import Rect

class Ball:
    def __init__(self, scale, screenw, screenh):
        self.default_x = (screenw >> 1) + scale
        self.default_y = screenh >> 1
        self.default_ball_pos = self.default_x, self.default_y

        ball_size = scale, scale
        self.rect = Rect(self.default_ball_pos, ball_size)

        self.default_speed = 3
        self.x_diff = self.default_speed
        self.y_diff = 0

        self.rate = 5
        self.frames_until_move = self.rate

        self.top_edge_line = 0, 0, screenw, 0
        self.bot_edge_line = 0, screenh, screenw, screenh

    def reset_position(self):
        self.rect.x = self.default_x
        self.rect.y = self.default_y

    def reset_velocity(self):
        self.x_diff = self.default_speed
        self.y_diff = 0
        self.frames_until_move = self.rate

    def increase_speed(self):
        if abs(self.x_diff) < self.rect.width:
            if self.x_diff > 0: self.x_diff += 1
            else: self.x_diff -= 1

    def bouce_off_edges(self):
        if self.rect.clipline(self.top_edge_line) != ():
            self.y_diff = -self.y_diff
        if self.rect.clipline(self.bot_edge_line) != ():
            self.y_diff = -self.y_diff

    def bounce_off_paddles(self, paddle1, paddle2):
        if self.rect.colliderect(paddle1):
            self.x_diff = -self.x_diff
            self.increase_speed()
        if self.rect.colliderect(paddle2):
            self.x_diff = -self.x_diff
            self.increase_speed()

    def shift_pos_horizontal(self):
        self.rect.x += self.x_diff

    def shift_pos_vertical(self):
        self.rect.y += self.y_diff

    def move(self, paddle1, paddle2):
        self.frames_until_move -= 1

        if self.frames_until_move <= 0:
            self.bounce_off_paddles(paddle1, paddle2)
            self.shift_pos_horizontal()

            self.bouce_off_edges()
            self.shift_pos_vertical()

            self.frames_until_move = self.rate