from pygame import Rect

class Player:
    def __init__(self, number, screenw, screenh):
        self.id = number
        self.screenw = screenw
        self.screenh = screenh

        self.score = 0

        if self.id == 1:
            self.goal_line = 0, 0, 0, self.screenh
        else:
            self.goal_line = self.screenw, 0, self.screenw, self.screenh

        paddle_size = pw, ph = 10, 50
        distance_from_edge = ph >> 1
        default_y = self.screenh >> 1
        if self.id == 1:
            paddle_pos = distance_from_edge, default_y
            self.paddle = Rect(paddle_pos, paddle_size)

            self.color = 0, 0, 255
        else:
            paddle_pos = self.screenw - distance_from_edge - pw, default_y
            self.paddle = Rect(paddle_pos, paddle_size)

            self.color = 255, 0, 0

    def within_top_bound(self):
        return self.paddle.y >= 0

    def within_bot_bound(self):
        return self.paddle.y <= self.screenh - self.paddle.height