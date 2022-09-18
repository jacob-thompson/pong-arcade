from pygame import Rect

class Ball:
    def __init__(self, scale, screenw, screenh):
        self.default_x = (screenw >> 1) + scale
        self.default_y = screenh >> 1
        self.default_ball_pos = self.default_x, self.default_y

        ball_size = scale, scale
        self.rect = Rect(self.default_ball_pos, ball_size)

        self.default_speed = 2
        self.x_diff = self.default_speed
        self.y_diff = 0

        self.rate = 5
        self.frames_until_move = self.rate

        self.top_edge_line = 0, 0, screenw, 0
        self.bot_edge_line = 0, screenh, screenw, screenh

    def reset_position(self):
        self.rect.x = self.default_x
        self.rect.y = self.default_y

    def reset_movement(self):
        self.x_diff = self.default_speed
        self.y_diff = 0
        self.frames_until_move = self.rate

    def reset(self):
        self.reset_position()
        self.reset_movement()

    def increase_speed(self):
        if abs(self.x_diff) < self.rect.w:
            if self.x_diff > 0: self.x_diff += 1
            else: self.x_diff -= 1

    def flip_direction_horizontal(self):
        self.x_diff = -self.x_diff

    def flip_direction_vertical(self):
        self.y_diff = -self.y_diff

    def get_collide_point(self, paddle):
        collision_rect = self.rect.clip(paddle)
        point = collision_rect.y + (collision_rect.h >> 1)

        return point

    def set_trajectory(self, paddle):
        psubd = paddle.h // 5
        outer_top = range(paddle.y, paddle.y + psubd)
        inner_top = range(paddle.y + psubd + 1, paddle.y + (psubd * 2))
        center = range(paddle.y + (psubd * 2) + 1, paddle.y + (psubd * 3))
        inner_bot = range(paddle.y + (psubd * 3) + 1, paddle.y + (psubd * 4))
        outer_bot = range(paddle.y + (psubd * 4) + 1, paddle.y + paddle.h)

        collide_point = self.get_collide_point(paddle)
        trajectory = 0

        if collide_point in outer_top:
            trajectory = 2
            if self.y_diff == 0: trajectory = -trajectory
        elif collide_point in inner_top:
            trajectory = 1
            if self.y_diff == 0: trajectory = -trajectory
        elif collide_point in center:
            trajectory = 0
        elif collide_point in inner_bot:
            trajectory = 1
        elif collide_point in outer_bot:
            trajectory = 2
        else:
            trajectory = 3

        if self.y_diff < 0: trajectory = -trajectory

        self.y_diff = trajectory

    def bounce_off_edges(self):
        if self.rect.clipline(self.top_edge_line) != ():
            self.flip_direction_vertical()

        if self.rect.clipline(self.bot_edge_line) != ():
            self.flip_direction_vertical()

    def bounce_off_paddles(self, paddle1, paddle2):
        if self.rect.colliderect(paddle1):
            self.increase_speed()
            self.flip_direction_horizontal()

            self.rect.x = paddle1.x + paddle1.w + 1

            self.set_trajectory(paddle1)

        if self.rect.colliderect(paddle2):
            self.increase_speed()
            self.flip_direction_horizontal()

            self.rect.x = paddle2.x - paddle2.w - 1

            self.set_trajectory(paddle2)

    def shift_pos_horizontal(self):
        self.rect.x += self.x_diff

    def shift_pos_vertical(self):
        self.rect.y += self.y_diff

    def move(self, paddle1, paddle2):
        self.frames_until_move -= 1

        if self.frames_until_move <= 0:
            self.bounce_off_paddles(paddle1, paddle2)
            self.shift_pos_horizontal()

            self.bounce_off_edges()
            self.shift_pos_vertical()

            self.frames_until_move = self.rate