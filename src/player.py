from pygame import Rect

class Player:
    def __init__(self, number):
        self.id = number

        self.screenw = 800
        self.screenh = 600

        self.score = 0
        self.winner = False

        self.goal_line = 0, 0, 0, 0
        self.paddle = Rect(0, 0, 0, 0)
        self.color = 0, 0, 0

    def reset_score(self):
        self.score = 0
        self.winner = False

    def set_color(self):
        if self.id == 1:
            self.color = 0, 0, 255
        else:
            self.color = 255, 0, 0

    def set_paddle_pos(self):
        paddle_size = pw, ph = 10, 50
        distance_from_edge = ph >> 1
        default_y = self.screenh >> 1

        if self.id == 1:
            paddle_pos = distance_from_edge, default_y
            self.paddle = Rect(paddle_pos, paddle_size)
        else:
            paddle_pos = self.screenw - distance_from_edge - pw, default_y
            self.paddle = Rect(paddle_pos, paddle_size)

    def set_goal_pos(self):
        if self.id == 1:
            self.goal_line = 0, 0, 0, self.screenh
        else:
            self.goal_line = self.screenw, 0, self.screenw, self.screenh

    def in_bound_top(self):
        defect = 15

        return self.paddle.y >= defect

    def in_bound_bot(self):
        defect = 15

        return self.paddle.y <= self.screenh - self.paddle.h - defect