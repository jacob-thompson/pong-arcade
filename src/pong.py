import ball, player

import pygame

from sys import exit

class Pong:
    def __init__(self):
        pygame.init()

        screensize = self.screenw, self.screenh = 800, 600
        self.surface = pygame.display.set_mode(screensize)

        self.font = pygame.font.Font("resources/visible/font.ttf", 50)
        self.font_big = pygame.font.Font("resources/visible/font.ttf", 100)
        self.font_small = pygame.font.Font("resources/visible/font.ttf", 10)

        self.p1 = player.Player(1)
        self.p2 = player.Player(0)
        self.ball = ball.Ball()

        self.ai_move_rate = 2
        self.frames_until_ai_move = self.ai_move_rate

        self.bg_color = 255, 255, 255
        self.fg_color = 0, 0, 0

        self.title = "Pong"

        self.show_menu = True
        self.paused = False

        self.mouse_pos = pygame.mouse.get_pos()

        self.clock = pygame.time.Clock()

        self.sound_paddle = pygame.mixer.Sound("resources/audible/paddle.wav")
        self.sound_wall = pygame.mixer.Sound("resources/audible/wall.wav")
        self.sound_score = pygame.mixer.Sound("resources/audible/score.wav")

        opt_h = 150
        self.menu_option1_rect = pygame.Rect(0, opt_h, self.screenw, opt_h)
        self.menu_option2_rect = pygame.Rect(0, opt_h * 2, self.screenw, opt_h)
        self.menu_option3_rect = pygame.Rect(0, opt_h * 3, self.screenw, opt_h)
        self.menu_option1_selected = False
        self.menu_option2_selected = False
        self.menu_option3_selected = True

    def set_window_properties(self):
        pygame.display.set_caption(self.title)

        icon = pygame.image.load("resources/visible/icon.png")
        pygame.display.set_icon(icon)

    def print_help_info(self):
        print("Pong -- https://github.com/jacob-thompson/Pong")

    def reset_game(self):
        self.p1.set_paddle_pos()
        self.p1.set_color()

        self.p2.set_paddle_pos()
        self.p2.set_color()

        self.p1.reset_score()
        self.p2.reset_score()

        if self.menu_option2_selected:
            self.p2.id = 2
        else:
            self.p2.id = 0

        self.ball.reset()

    def start_new_game(self):
        self.show_menu = False
        self.paused = False

        self.reset_game()

        pygame.mouse.set_visible(False)

    def keyboard_select(self, button):
        if not self.show_menu: return

        if button == pygame.K_1:
            self.menu_option1_selected = True

        if button == pygame.K_2:
            self.menu_option2_selected = True

        if button == pygame.K_3:
            self.menu_option3_selected = not self.menu_option3_selected

            if self.menu_option3_selected: self.sound_paddle.play()

        if self.menu_option1_selected or self.menu_option2_selected:
            self.start_new_game()

    def mouse_select(self, pos, button):
        if not self.show_menu: return
        if button != 1: return

        if self.menu_option1_rect.collidepoint(pos):
            self.menu_option1_selected = True

        if self.menu_option2_rect.collidepoint(pos):
            self.menu_option2_selected = True

        if self.menu_option3_rect.collidepoint(pos):
            self.menu_option3_selected = not self.menu_option3_selected

            if self.menu_option3_selected: self.sound_paddle.play()

        if self.menu_option1_selected or self.menu_option2_selected:
            self.start_new_game()

    def go_to_menu(self):
        self.menu_option1_selected = False
        self.menu_option2_selected = False

        self.show_menu = True

    def toggle_pause(self):
        if not self.show_menu:
            self.paused = not self.paused

    def handle(self, event):
        if event.type == pygame.QUIT: exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: exit()
            elif event.key == pygame.K_p: self.toggle_pause()
            elif event.key == pygame.K_m: self.go_to_menu()
            else: self.keyboard_select(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_select(event.pos, event.button)

    def give_victory(self, player):
        player.winner = True

        self.go_to_menu()

        pygame.mouse.set_visible(True)

    def check_for_winner(self, player):
        if player.score >= 10:
            self.give_victory(player)

    def check_for_score(self):
        p1_score = self.ball.rect.right >= self.screenw
        p2_score = self.ball.rect.left <= 0

        if p1_score:
            self.p1.score += 1
            self.ball.reset()

            if self.menu_option3_selected: self.sound_score.play()

            self.check_for_winner(self.p1)

        if p2_score:
            self.p2.score += 1
            self.ball.reset()

            if self.menu_option3_selected: self.sound_score.play()

            self.check_for_winner(self.p2)

    def tick(self, frame_rate):
        self.clock.tick(frame_rate)

    def ensure_boundaries(self):
        self.p1.ensure_in_bound_bot()
        self.p1.ensure_in_bound_top()

        self.p2.ensure_in_bound_bot()
        self.p2.ensure_in_bound_top()

    def ai_paddle_movement(self):
        if self.ball.x_diff < 0:
            speed = 1
        else:
            speed = 6

        can_move_up = self.ball.rect.bottom < self.p2.paddle.centery
        can_move_down = self.ball.rect.top > self.p2.paddle.centery

        if can_move_up:
            self.p2.paddle.y -= speed
        elif can_move_down:
            self.p2.paddle.y += speed

    def update_paddle_position(self):
        keys = pygame.key.get_pressed()

        speed = 10

        if keys[pygame.K_w]:
            self.p1.paddle.y -= speed

        if keys[pygame.K_s]:
            self.p1.paddle.y += speed

        one_player = self.p2.id == 0

        if keys[pygame.K_UP] and one_player:
            self.p1.paddle.y -= speed
        elif keys[pygame.K_UP]:
            self.p2.paddle.y -= speed

        if keys[pygame.K_DOWN] and one_player:
            self.p1.paddle.y += speed
        elif keys[pygame.K_DOWN]:
            self.p2.paddle.y += speed

        if one_player:
            self.ai_paddle_movement()

        self.ensure_boundaries()

    def update_ball_position(self):
        self.check_for_score()

        if self.ball.bflag_edge and self.menu_option3_selected:
            self.sound_wall.play()

        if self.ball.bflag_paddle and self.menu_option3_selected:
            self.sound_paddle.play()

        self.ball.move(self.p1.paddle, self.p2.paddle)

    def draw_background(self):
        self.surface.fill(self.bg_color)

    def draw_center_line(self):
        linew = 10
        lineh = linew << 1
        top = self.screenh
        left = (self.screenw >> 1) - (linew >> 1)
        while top >= 0:
            top -= lineh >> 1
            center_rect = (left, top, linew, lineh)

            pygame.draw.rect(self.surface, self.fg_color, center_rect)
            top -= lineh

    def draw_ball(self):
        pygame.draw.rect(self.surface, self.fg_color, self.ball.rect)

    def draw_scores(self):
        score1 = self.font.render(str(self.p1.score), 1, self.p1.color)
        s1_pos = self.screenw >> 2, 0
        s1_rect = score1.get_rect(midtop = s1_pos)
        self.surface.blit(score1, s1_rect)

        score2 = self.font.render(str(self.p2.score), 1, self.p2.color)
        s2_pos = (self.screenw >> 1) + (self.screenw >> 2), 0
        s2_rect = score2.get_rect(midtop = s2_pos)
        self.surface.blit(score2, s2_rect)

    def draw_paddles(self):
        pygame.draw.rect(self.surface, self.p1.color, self.p1.paddle)
        pygame.draw.rect(self.surface, self.p2.color, self.p2.paddle)

    def draw_game(self):
        self.draw_background()
        self.draw_center_line()
        self.draw_ball()
        self.draw_scores()
        self.draw_paddles()

    def draw_title(self):
        text = self.font_big.render(self.title, 1, self.fg_color)
        tpos = self.screenw >> 1, 15
        trect = text.get_rect(midtop = tpos)
        self.surface.blit(text, trect)

    def draw_options(self):
        option1 = "(1) One Player"
        option1_color = 0, 0, 255
        option1_text = self.font.render(option1, 1, option1_color)
        option1_pos = self.menu_option1_rect.center
        option1_rect = option1_text.get_rect(center = option1_pos)

        option2 = "(2) Two Players"
        option2_color = 255, 0, 0
        option2_text = self.font.render(option2, 1, option2_color)
        option2_pos = self.menu_option2_rect.center
        option2_rect = option2_text.get_rect(center = option2_pos)

        if self.menu_option3_selected:
            option3 = "(x) Sound"
        else:
            option3 = "( ) Sound"

        option3_text = self.font.render(option3, 1, self.fg_color)
        option3_pos = self.menu_option3_rect.center
        option3_rect = option3_text.get_rect(center = option3_pos)

        self.surface.blit(option1_text, option1_rect)
        self.surface.blit(option2_text, option2_rect)
        self.surface.blit(option3_text, option3_rect)

    def draw_info(self):
        disclaimer = "MIT License Copyright (c) 2022 Jacob Alexander Thompson"

        text = self.font_small.render(disclaimer, 1, self.fg_color)
        tpos = 3, self.screenh
        trect = text.get_rect(bottomleft = tpos)
        self.surface.blit(text, trect)

    def draw_menu(self):
        self.draw_background()
        self.draw_title()
        self.draw_options()
        self.draw_info()

    def draw_frame(self):
        if self.show_menu:
            self.draw_menu()
        else:
            self.draw_game()

    def update_frame(self):
        pygame.display.flip()