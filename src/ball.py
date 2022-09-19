from pygame import Rect

from random import randint

class Ball:
    def __init__(self):
        screenw = 800
        screenh = 600

        self.default_x = (screenw >> 1) + 10
        self.default_y = screenh >> 1
        self.default_ball_pos = self.default_x, self.default_y

        ball_size = 10, 10
        self.rect = Rect(self.default_ball_pos, ball_size)

        self.default_speed = 6
        self.x_diff = self.default_speed
        self.y_diff = 0

        self.top_edge_line = 0, 0, screenw, 0
        self.bot_edge_line = 0, screenh, screenw, screenh

        self.bflag_edge = False
        self.bflag_paddle = False

    def reset_position(self):
        self.rect.x = self.default_x
        self.rect.y = self.default_y

    def reset_movement(self):
        self.x_diff = self.default_speed
        self.y_diff = 0

    def reset_flags(self):
        self.bflag_edge = False
        self.bflag_paddle = False

    def reset(self):
        self.reset_position()
        self.reset_movement()
        self.reset_flags()

    def increase_speed(self):
        if abs(self.x_diff) < self.rect.w << 1:
            if self.x_diff > 0: self.x_diff += 1
            else: self.x_diff -= 1

    def flip_direction_horizontal(self):
        self.x_diff = -self.x_diff

    def flip_direction_vertical(self):
        self.y_diff = -self.y_diff

    def get_collision_point(self, paddle):
        collision_rect = self.rect.clip(paddle)
        point = collision_rect.y + (collision_rect.h >> 1)

        return point

    def coin_flip(self):
        return randint(1, 2) == 1

    def set_trajectory(self, paddle):
        psubd = paddle.h // 5
        outer_top = range(paddle.y, paddle.y + psubd)
        inner_top = range(paddle.y + psubd + 1, paddle.y + (psubd * 2))
        center = range(paddle.y + (psubd * 2) + 1, paddle.y + (psubd * 3))
        inner_bot = range(paddle.y + (psubd * 3) + 1, paddle.y + (psubd * 4))
        outer_bot = range(paddle.y + (psubd * 4) + 1, paddle.y + paddle.h)

        collision_point = self.get_collision_point(paddle)

        if collision_point < paddle.y:
            trajectory = 6
            if self.y_diff == 0: trajectory = -trajectory
        elif collision_point in outer_top:
            trajectory = 4
            if self.y_diff == 0: trajectory = -trajectory
        elif collision_point in inner_top:
            trajectory = 2
            if self.y_diff == 0: trajectory = -trajectory
        elif collision_point in center:
            if self.coin_flip(): trajectory = randint(1, 2)
            else: trajectory = 0
        elif collision_point in inner_bot:
            trajectory = 2
        elif collision_point in outer_bot:
            trajectory = 4
        elif collision_point > paddle.y + paddle.h:
            trajectory = 6
        else:
            trajectory = randint(0, 6)

        if self.y_diff < 0: trajectory = -trajectory

        self.y_diff = trajectory

    def bounce_off_edges(self):
        if self.rect.clipline(self.top_edge_line) != ():
            self.flip_direction_vertical()

            self.bflag_edge = True

        if self.rect.clipline(self.bot_edge_line) != ():
            self.flip_direction_vertical()

            self.bflag_edge = True

    def bounce_off_paddles(self, paddle1, paddle2):
        if self.rect.colliderect(paddle1):
            self.increase_speed()
            self.flip_direction_horizontal()

            self.bflag_paddle = True

            self.rect.x = paddle1.x + paddle1.w + 1

            self.set_trajectory(paddle1)

        if self.rect.colliderect(paddle2):
            self.increase_speed()
            self.flip_direction_horizontal()

            self.bflag_paddle = True

            self.rect.x = paddle2.x - paddle2.w - 1

            self.set_trajectory(paddle2)

    def shift_pos_horizontal(self):
        self.rect.x += self.x_diff

    def shift_pos_vertical(self):
        self.rect.y += self.y_diff

    def move(self, paddle1, paddle2):
        self.reset_flags()

        self.bounce_off_paddles(paddle1, paddle2)
        self.shift_pos_horizontal()

        self.bounce_off_edges()
        self.shift_pos_vertical()