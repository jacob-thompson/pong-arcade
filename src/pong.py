import player
import ball

import pygame

from sys import exit

class Pong:
    def __init__(self):
        pygame.init()

        winsize = self.width, self.height = 800, 600
        self.surface = pygame.display.set_mode(winsize)

        self.font = pygame.font.Font("resources/font.ttf", 50)

        self.p1 = player.Player(1, self.width, self.height)
        self.p2 = player.Player(0, self.width, self.height)

        self.ball = ball.Ball(10, self.width, self.height)

        self.bg_color = 255, 255, 255
        self.fg_color = 0, 0, 0

    def set_window_properties(self):
        pygame.display.set_caption("Pong")
        icon = pygame.image.load("resources/icon.png")
        pygame.display.set_icon(icon)

    def print_help_info(self):
        print("Pong -- https://github.com/jacob-thompson/Pong")

    def handle(self, event):
        if event.type == pygame.QUIT: exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: exit()

    def check_for_score(self):
        if self.ball.rect.clipline(self.p1.goal_line) != ():
            self.p2.score += 1
            self.ball.reset_position()
            self.ball.reset_velocity()

        if self.ball.rect.clipline(self.p2.goal_line) != ():
            self.p1.score += 1
            self.ball.reset_position()
            self.ball.reset_velocity()

    def update_paddle_position(self):
        keys = pygame.key.get_pressed()

        within_top_bound = self.p1.paddle.y >= 0
        within_bot_bound = self.p1.paddle.y <= self.height - self.p1.paddle.height

        if keys[pygame.K_w] and self.p1.within_top_bound():
            self.p1.paddle.y -= 1
        if keys[pygame.K_s] and self.p1.within_bot_bound():
            self.p1.paddle.y += 1

    def update_ball_position(self):
        self.check_for_score()
        self.ball.move(self.p1.paddle, self.p2.paddle)

    def draw_background(self):
        self.surface.fill(self.bg_color)

    def draw_center_line(self):
        linew = 10
        lineh = linew << 1
        top = self.height
        left = (self.width >> 1) - (linew >> 1)
        while top >= 0:
            top -= lineh >> 1
            center_rect = (left, top, linew, lineh)

            pygame.draw.rect(self.surface, self.fg_color, center_rect)
            top -= lineh

    def draw_ball(self):
        pygame.draw.rect(self.surface, self.fg_color, self.ball.rect)

    def draw_scores(self):
        score1 = self.font.render(str(self.p1.score), 1, self.p1.color)
        s1_pos = self.width >> 2, 0
        s1_rect = score1.get_rect(midtop = s1_pos)
        self.surface.blit(score1, s1_rect)

        score2 = self.font.render(str(self.p2.score), 1, self.p2.color)
        s2_pos = (self.width >> 1) + (self.width >> 2), 0
        s2_rect = score2.get_rect(midtop = s2_pos)
        self.surface.blit(score2, s2_rect)

    def draw_paddles(self):
        pygame.draw.rect(self.surface, self.p1.color, self.p1.paddle)
        pygame.draw.rect(self.surface, self.p2.color, self.p2.paddle)

    def draw_frame(self):
        self.draw_background()
        self.draw_center_line()
        self.draw_ball()
        self.draw_scores()
        self.draw_paddles()

    def update_frame(self):
        pygame.display.flip()