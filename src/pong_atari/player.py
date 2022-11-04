from .meta import SCREEN_W, SCREEN_H

from pygame import Rect

class Player:
    def __init__(self, number, color):
        self.id = number
        self.color = color

        self.score = 0
        self.winner = False

        self.paddle = Rect(0, 0, 10, 50)

    def reset_score(self):
        self.score = 0
        self.winner = False

    def set_color(self):
        if self.id == 1:
            self.color = 0, 0, 255
        else:
            self.color = 255, 0, 0

    def set_paddle_pos(self):
        distance_from_edge = self.paddle.h >> 1
        default_y = SCREEN_H >> 1

        if self.id == 1:
            paddle_pos = distance_from_edge, default_y
            self.paddle = Rect(paddle_pos, self.paddle.size)
        else:
            paddle_pos = SCREEN_W - distance_from_edge - self.paddle.w, default_y
            self.paddle = Rect(paddle_pos, self.paddle.size)

    def ensure_in_bound_top(self):
        defect = 20

        if self.paddle.y < defect:
            self.paddle.y = defect

    def ensure_in_bound_bot(self):
        defect = 20

        if self.paddle.y > SCREEN_H - self.paddle.h - defect:
            self.paddle.y = SCREEN_H - self.paddle.h - defect