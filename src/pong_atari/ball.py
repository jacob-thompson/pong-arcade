from .meta import SCREEN_W, SCREEN_H

from random import randint

from pygame import Rect

class Ball:
    def __init__(self):
        self.default_x = (SCREEN_W >> 1) + 10
        self.default_y = SCREEN_H >> 1
        self.default_ball_pos = self.default_x, self.default_y

        ball_size = 10, 10
        self.rect = Rect(self.default_ball_pos, ball_size)

        self.default_speed = self.x_diff = 6
        self.y_diff = 0

        self.top_edge_line = 0, 0, SCREEN_W, 0
        self.bot_edge_line = 0, SCREEN_H, SCREEN_W, SCREEN_H

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
        increment = 2

        if abs(self.x_diff) < self.rect.w << 1:
            if self.x_diff > 0: self.x_diff += increment
            else: self.x_diff -= increment

    def flip_direction_horizontal(self):
        self.x_diff = -self.x_diff

    def flip_direction_vertical(self):
        self.y_diff = -self.y_diff

    def get_collision_point(self, paddle):
        collision_rect = self.rect.clip(paddle)
        point = collision_rect.y + (collision_rect.h >> 1)

        return point

    def trajectory(self, paddle):
        psubd = paddle.h // 5
        outer_top = range(paddle.y, paddle.y + psubd)
        inner_top = range(paddle.y + psubd + 1, paddle.y + (psubd * 2))
        center = range(paddle.y + (psubd * 2) + 1, paddle.y + (psubd * 3))
        inner_bot = range(paddle.y + (psubd * 3) + 1, paddle.y + (psubd * 4))
        outer_bot = range(paddle.y + (psubd * 4) + 1, paddle.y + paddle.h)

        collision_point = self.get_collision_point(paddle)

        min_t = 0
        low_t = 2
        mid_t = 5
        max_t = 8

        if collision_point < paddle.y:
            trajectory = max_t
            if self.y_diff == 0: trajectory = -trajectory
        elif collision_point in outer_top:
            trajectory = mid_t
            if self.y_diff == 0: trajectory = -trajectory
        elif collision_point in inner_top:
            trajectory = low_t
            if self.y_diff == 0: trajectory = -trajectory
        elif collision_point in center:
            if self.y_diff == 0: trajectory = randint(-low_t, low_t)
            else: trajectory = 0
        elif collision_point in inner_bot:
            trajectory = low_t
        elif collision_point in outer_bot:
            trajectory = mid_t
        elif collision_point > paddle.y + paddle.h:
            trajectory = max_t
        else:
            trajectory = randint(min_t, max_t)

        if self.y_diff < 0: trajectory = -trajectory

        return trajectory

    def bounce_off_edges(self):
        if self.rect.clipline(self.top_edge_line) != ():
            self.flip_direction_vertical()

            self.bflag_edge = True

        if self.rect.clipline(self.bot_edge_line) != ():
            self.flip_direction_vertical()

            self.bflag_edge = True

    def bounce_off_paddles(self, paddle1, paddle2):
        if self.rect.colliderect(paddle1):
            self.bflag_paddle = True

            self.increase_speed()
            self.flip_direction_horizontal()
            self.rect.x = paddle1.right + 1

            self.y_diff = self.trajectory(paddle1)

        if self.rect.colliderect(paddle2):
            self.bflag_paddle = True

            self.increase_speed()
            self.flip_direction_horizontal()
            self.rect.x = paddle2.left - self.rect.w - 1

            self.y_diff = self.trajectory(paddle2)

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