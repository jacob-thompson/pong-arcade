from pygame import Rect

class Player:
    def __init__(self, number, screenw, screenh):
        self.id = number

        self.score = 0

        paddle_size = pw, ph = 10, 50
        distance_from_edge = ph >> 1
        default_y = screenh >> 1
        if self.id == 1:
            paddle_pos = distance_from_edge, default_y
            self.paddle = Rect(paddle_pos, paddle_size)

            self.color = 0, 0, 255
        else:
            paddle_pos = screenw - distance_from_edge - pw, default_y
            self.paddle = Rect(paddle_pos, paddle_size)

            self.color = 255, 0, 0