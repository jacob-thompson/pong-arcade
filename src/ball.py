from pygame import Rect

class Ball:
    def __init__(self, scale, screenw, screenh):
        self.default_x = (screenw >> 1) + scale
        self.default_y = screenh >> 1
        self.default_ball_pos = self.default_x, self.default_y

        ball_size = scale, scale
        self.rect = Rect(self.default_ball_pos, ball_size)

        self.default_rate = 8
        self.default_speed = 1

        self.x_frames_per_move = self.default_rate
        self.x_frames_until_move = self.x_frames_per_move
        self.x_diff = self.default_speed

        self.y_frames_per_move = self.default_rate
        self.y_frames_until_move = self.y_frames_per_move
        self.y_diff = 0

        self.top_edge = 0, 0, screenw, 0
        self.bot_edge = 0, screenh, screenw, screenh

    def reset_position(self):
        self.rect.x = self.default_x
        self.rect.y = self.default_y

    def reset_velocity(self):
        self.x_frames_per_move = self.default_rate
        self.x_frames_until_move = self.x_frames_per_move
        self.x_diff = self.default_speed

        self.y_frames_per_move = self.default_rate
        self.y_frames_until_move = self.y_frames_per_move
        self.y_diff = 0

    def bouce_off_edges(self):
        if self.rect.clipline(self.top_edge) != ():
            self.y_diff = -self.y_diff

        if self.rect.clipline(self.bot_edge) != ():
            self.y_diff = -self.y_diff

    def bounce_off_paddles(self, paddle1, paddle2):
        if self.rect.colliderect(paddle1):
            self.x_diff = -self.x_diff
        if self.rect.colliderect(paddle2):
            self.x_diff = -self.x_diff

    def shift_horizontal(self):
        self.rect.x += self.x_diff
        self.x_frames_until_move = self.x_frames_per_move

    def shift_vertical(self):
        self.rect.y += self.y_diff
        self.y_frames_until_move = self.y_frames_per_move

    def move(self, paddle1, paddle2):
        self.x_frames_until_move -= 1
        self.y_frames_until_move -= 1

        self.bouce_off_edges()
        self.bounce_off_paddles(paddle1, paddle2)

        if self.x_frames_until_move <= 0:
            self.bounce_off_paddles(paddle1, paddle2)
            self.shift_horizontal()

        if self.y_frames_until_move <= 0:
            self.bouce_off_edges()
            self.shift_vertical()