from pygame import Rect

class Ball:
    def __init__(self, scale, screenw, screenh):
        self.ball_scale = scale

        default_x = (screenw >> 1) + self.ball_scale
        default_y = screenh >> 1
        ball_pos = default_x, default_y
        ball_size = self.ball_scale, self.ball_scale
        self.rect = Rect(ball_pos, ball_size)