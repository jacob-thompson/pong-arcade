from .meta import SCREEN_W, SCREEN_H, TITLE, FPS
from .player import Player
from .ball import Ball

from os import path
from sys import exit

import pygame

class Pong:
    def __init__(self):
        pygame.display.init()
        size = SCREEN_W, SCREEN_H
        self.surface = pygame.display.set_mode(size)

        self.clock = pygame.time.Clock()

        self.dir, self.file = path.split(__file__)

        pygame.font.init()
        font_file = path.join(self.dir, "data", "gfx", "atari.otf")
        self.font = pygame.font.Font(font_file, 50)
        self.font_big = pygame.font.Font(font_file, 100)
        self.font_small = pygame.font.Font(font_file, 20)
        self.font_tiny = pygame.font.Font(font_file, 10)

        pygame.mixer.init()
        paddle_file = path.join(self.dir, "data", "sfx", "paddle.wav")
        self.sound_paddle = pygame.mixer.Sound(paddle_file)
        wall_file = path.join(self.dir, "data", "sfx", "wall.wav")
        self.sound_wall = pygame.mixer.Sound(wall_file)
        score_file = path.join(self.dir, "data", "sfx", "score.wav")
        self.sound_score = pygame.mixer.Sound(score_file)

        opt_h = 150
        self.help_rect = pygame.Rect(0, 0, SCREEN_W, opt_h)
        self.opt1_rect = pygame.Rect(0, opt_h, SCREEN_W, opt_h)
        self.opt2_rect = pygame.Rect(0, opt_h * 2, SCREEN_W, opt_h)
        self.opt3_rect = pygame.Rect(0, opt_h * 3, SCREEN_W, opt_h)

        self.show_help_menu = False
        self.opt1_selected = False
        self.opt2_selected = False
        self.opt3_selected = True

        self.show_menu = True
        self.paused = False

        self.show_win_screen = False

        self.bg_color = 255, 255, 255
        self.fg_color = 0, 0, 0
        self.red = 255, 0, 0
        self.blue = 0, 0, 255

        self.p1 = Player(1, self.blue)
        self.p2 = Player(0, self.red)
        self.ball = Ball()

    def set_window_properties(self):
        pygame.display.set_caption(TITLE)

        icon_file = path.join(self.dir, "data", "gfx", "logo.png")
        icon = pygame.image.load(icon_file)

        pygame.display.set_icon(icon)

    def print_info(self):
        print("Thanks for playing Pong! https://github.com/jacob-thompson/pong-arcade")

    def reset_game(self):
        self.p1.set_paddle_pos()
        self.p1.set_color()

        self.p2.set_paddle_pos()
        self.p2.set_color()

        self.p1.reset_score()
        self.p2.reset_score()

        if self.opt2_selected:
            self.p2.id = 2
        else:
            self.p2.id = 0

        self.ball.reset()

    def start_new_game(self):
        self.show_menu = False
        self.paused = False

        self.reset_game()

        pygame.mouse.set_visible(False)

    def menu_keyboard_select(self, button):
        if self.show_win_screen:
            self.show_win_screen = not self.show_win_screen
            self.go_to_menu()
            return

        if not self.show_menu: return

        if self.show_help_menu:
            self.show_help_menu = not self.show_help_menu
        elif button == pygame.K_c:
            self.show_help_menu = not self.show_help_menu
        elif button == pygame.K_1 and not self.show_help_menu:
            self.opt1_selected = True
        elif button == pygame.K_2 and not self.show_help_menu:
            self.opt2_selected = True
        elif button == pygame.K_3 and not self.show_help_menu:
            self.opt3_selected = not self.opt3_selected

            if self.opt3_selected: self.sound_paddle.play()

        if self.opt1_selected or self.opt2_selected:
            self.start_new_game()

    def menu_mouse_select(self, pos, button):
        if self.show_win_screen:
            self.show_win_screen = not self.show_win_screen
            self.go_to_menu()
            return

        if not self.show_menu: return
        if button != 1: return

        if self.show_help_menu:
            self.show_help_menu = not self.show_help_menu
        elif self.help_rect.collidepoint(pos):
            self.show_help_menu = not self.show_help_menu
        elif self.opt1_rect.collidepoint(pos) and not self.show_help_menu:
            self.opt1_selected = True
        elif self.opt2_rect.collidepoint(pos) and not self.show_help_menu:
            self.opt2_selected = True
        elif self.opt3_rect.collidepoint(pos) and not self.show_help_menu:
            self.opt3_selected = not self.opt3_selected

            if self.opt3_selected: self.sound_paddle.play()

        if self.opt1_selected or self.opt2_selected:
            self.start_new_game()

    def go_to_menu(self):
        self.opt1_selected = False
        self.opt2_selected = False

        self.show_menu = True

    def toggle_pause(self):
        if not self.show_menu:
            self.paused = not self.paused

    def handle_event(self, event):
        if event.type == pygame.QUIT: exit()

        if event.type == pygame.KEYDOWN:
            self.menu_keyboard_select(event.key)

            close = event.key == pygame.K_ESCAPE
            pause = event.key == pygame.K_p or event.key == pygame.K_q
            menu = event.key == pygame.K_m or event.key == pygame.K_z

            if close: exit()
            elif pause: self.toggle_pause()
            elif menu: self.go_to_menu()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.menu_mouse_select(event.pos, event.button)

    def is_winner(self):
        return self.p1.winner or self.p2.winner

    def game_in_progress(self):
        return not self.show_menu and not self.paused and not self.is_winner()

    def give_victory(self, player):
        player.winner = True
        self.show_win_screen = True

        pygame.mouse.set_visible(True)

    def check_for_winner(self, player):
        if player.score >= 10:
            self.give_victory(player)

    def check_for_score(self):
        p1_score = self.ball.rect.right >= SCREEN_W
        p2_score = self.ball.rect.left <= 0

        if p1_score:
            self.p1.score += 1
            self.ball.reset()

            if self.opt3_selected: self.sound_score.play()

            self.check_for_winner(self.p1)

        if p2_score:
            self.p2.score += 1
            self.ball.reset()

            if self.opt3_selected: self.sound_score.play()

            self.check_for_winner(self.p2)

    def tick(self):
        self.clock.tick(FPS)

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

        if keys[pygame.K_i] and one_player:
            self.p1.paddle.y -= speed
        elif keys[pygame.K_i]:
            self.p2.paddle.y -= speed

        if keys[pygame.K_k] and one_player:
            self.p1.paddle.y += speed
        elif keys[pygame.K_k]:
            self.p2.paddle.y += speed

        if one_player:
            self.ai_paddle_movement()

        self.ensure_boundaries()

    def update_ball_position(self):
        self.check_for_score()

        if self.ball.bflag_edge and self.opt3_selected:
            self.sound_wall.play()

        if self.ball.bflag_paddle and self.opt3_selected:
            self.sound_paddle.play()

        self.ball.move(self.p1.paddle, self.p2.paddle)

    def draw_background(self):
        self.surface.fill(self.bg_color)

    def draw_center_line(self):
        linew = 10
        lineh = linew << 1
        top = SCREEN_H
        left = (SCREEN_W >> 1) - (linew >> 1)
        while top >= 0:
            top -= lineh >> 1
            center_rect = (left, top, linew, lineh)

            pygame.draw.rect(self.surface, self.fg_color, center_rect)
            top -= lineh

    def draw_ball(self):
        pygame.draw.rect(self.surface, self.fg_color, self.ball.rect)

    def draw_scores(self):
        score1 = self.font.render(str(self.p1.score), 1, self.p1.color)
        s1_pos = SCREEN_W >> 2, 0
        s1_rect = score1.get_rect(midtop = s1_pos)
        self.surface.blit(score1, s1_rect)

        score2 = self.font.render(str(self.p2.score), 1, self.p2.color)
        s2_pos = (SCREEN_W >> 1) + (SCREEN_W >> 2), 0
        s2_rect = score2.get_rect(midtop = s2_pos)
        self.surface.blit(score2, s2_rect)

    def draw_paddles(self, help_menu=False):
        if help_menu:
            self.p1.paddle.center = SCREEN_W >> 2, SCREEN_H >> 1
            self.p2.paddle.center = (SCREEN_W >> 2) * 3, SCREEN_H >> 1

        pygame.draw.rect(self.surface, self.p1.color, self.p1.paddle)
        pygame.draw.rect(self.surface, self.p2.color, self.p2.paddle)

    def draw_game(self):
        self.draw_background()
        self.draw_center_line()
        self.draw_ball()
        self.draw_scores()
        self.draw_paddles()

    def draw_title(self):
        text = self.font_big.render(TITLE, 1, self.fg_color)
        tpos = self.help_rect.center
        trect = text.get_rect(center = tpos)
        self.surface.blit(text, trect)

    def draw_options(self):
        option1 = "(1) One Player"
        option1_text = self.font.render(option1, 1, self.blue)
        option1_rect = option1_text.get_rect(center = self.opt1_rect.center)

        option2 = "(2) Two Players"
        option2_text = self.font.render(option2, 1, self.red)
        option2_rect = option2_text.get_rect(center = self.opt2_rect.center)

        if self.opt3_selected:
            option3 = "(3) Sound: On"
        else:
            option3 = "(3) Sound: Off"

        option3_text = self.font.render(option3, 1, self.fg_color)
        option3_rect = option3_text.get_rect(center = self.opt3_rect.center)

        self.surface.blit(option1_text, option1_rect)
        self.surface.blit(option2_text, option2_rect)
        self.surface.blit(option3_text, option3_rect)

        controls = "Press C or click here for controls"

        ctext = self.font_tiny.render(controls, 1, self.fg_color)
        ctpos = SCREEN_W - 3, 0
        ctrect = ctext.get_rect(topright = ctpos)

        self.surface.blit(ctext, ctrect)

    def draw_info(self):
        disclaimer = "MIT License Copyright (c) 2022 Jacob Alexander Thompson"

        dtext = self.font_tiny.render(disclaimer, 1, self.fg_color)
        dtpos = 3, SCREEN_H
        dtrect = dtext.get_rect(bottomleft = dtpos)
        self.surface.blit(dtext, dtrect)

    def draw_menu(self):
        self.draw_background()
        self.draw_title()
        self.draw_options()
        self.draw_info()

    def draw_arrow(self, surface, start_pos, end_pos, color):
        body_w = 1
        head_w = 20
        head_h = 10

        start = pygame.math.Vector2(start_pos)
        end = pygame.math.Vector2(end_pos)

        arrow = start - end
        angle = arrow.angle_to(pygame.Vector2(0, -1))
        body_len = int(arrow.length()) - head_h

        head_verts = [
            pygame.Vector2(0, head_h >> 1),
            pygame.Vector2(head_w >> 1, -head_h >> 1),
            pygame.Vector2(-head_w >> 1, -head_h >> 1),
        ]

        translation = pygame.Vector2(0, arrow.length() - (head_h >> 1)).rotate(-angle)
        for i in range(len(head_verts)):
            head_verts[i].rotate_ip(-angle)
            head_verts[i] += translation
            head_verts[i] += start

        pygame.draw.polygon(surface, color, head_verts)

        if arrow.length() >= head_h:
            body_verts = [
                pygame.Vector2(-body_w >> 1, body_len >> 1),
                pygame.Vector2(body_w >> 1, body_len >> 1),
                pygame.Vector2(body_w >> 1, -body_len >> 1),
                pygame.Vector2(-body_w >> 1, -body_len >> 1),
            ]

            translation = pygame.Vector2(0, body_len >> 1).rotate(-angle)
            for i in range(len(body_verts)):
                body_verts[i].rotate_ip(-angle)
                body_verts[i] += translation
                body_verts[i] += start

            pygame.draw.polygon(surface, color, body_verts)

    def draw_help_arrows(self):
        gap = 30
        arrow_len = 100

        p1_up_spos = self.p1.paddle.centerx, self.p1.paddle.top - gap
        p1_up_epos = self.p1.paddle.centerx, self.p1.paddle.top - gap - arrow_len
        p1_down_spos = self.p1.paddle.centerx, self.p1.paddle.bottom + gap
        p1_down_epos = self.p1.paddle.centerx, self.p1.paddle.bottom + gap + arrow_len

        p2_up_spos = self.p2.paddle.centerx, self.p2.paddle.top - gap
        p2_up_epos = self.p2.paddle.centerx, self.p2.paddle.top - gap - arrow_len
        p2_down_spos = self.p2.paddle.centerx, self.p2.paddle.bottom + gap
        p2_down_epos = self.p2.paddle.centerx, self.p2.paddle.bottom + gap + arrow_len

        self.draw_arrow(self.surface, p1_up_spos, p1_up_epos, self.fg_color)
        self.draw_arrow(self.surface, p1_down_spos, p1_down_epos, self.fg_color)
        self.draw_arrow(self.surface, p2_up_spos, p2_up_epos, self.fg_color)
        self.draw_arrow(self.surface, p2_down_spos, p2_down_epos, self.fg_color)

    def draw_help_text(self):
        hmenu = "Pong Controls"
        hmenu_text = self.font_small.render(hmenu, 1, self.fg_color)
        hmenu_pos = SCREEN_W >> 1, 0
        hmenu_rect = hmenu_text.get_rect(midtop = hmenu_pos)
        self.surface.blit(hmenu_text, hmenu_rect)

        pause = "P or Q  -  Pause"
        pause_text = self.font_small.render(pause, 1, self.fg_color)
        pause_pos = self.p1.paddle.centerx, SCREEN_H >> 3
        pause_rect = pause_text.get_rect(center = pause_pos)
        self.surface.blit(pause_text, pause_rect)

        menu = "Menu  -  M or Z"
        menu_text = self.font_small.render(menu, 1, self.fg_color)
        menu_pos = self.p2.paddle.centerx, SCREEN_H >> 3
        menu_rect = menu_text.get_rect(center = menu_pos)
        self.surface.blit(menu_text, menu_rect)

        cmdleft = (SCREEN_W >> 3) * 3
        cmdright = (SCREEN_W >> 3) * 5
        cmdup = SCREEN_H >> 2
        cmddown = cmdup * 3

        wkey = "W"
        wkey_text = self.font_small.render(wkey, 1, self.fg_color)
        wkey_pos = cmdleft, cmdup
        wkey_rect = wkey_text.get_rect(center = wkey_pos)
        self.surface.blit(wkey_text, wkey_rect)

        skey = "S"
        skey_text = self.font_small.render(skey, 1, self.fg_color)
        skey_pos = cmdleft, cmddown
        skey_rect = skey_text.get_rect(center = skey_pos)
        self.surface.blit(skey_text, skey_rect)

        ikey = "I"
        ikey_text = self.font_small.render(ikey, 1, self.fg_color)
        ikey_pos = cmdright, cmdup
        ikey_rect = ikey_text.get_rect(center = ikey_pos)
        self.surface.blit(ikey_text, ikey_rect)

        kkey = "K"
        kkey_text = self.font_small.render(kkey, 1, self.fg_color)
        kkey_pos = cmdright, cmddown
        kkey_rect = kkey_text.get_rect(center = kkey_pos)
        self.surface.blit(kkey_text, kkey_rect)

        p1 = "Player 1"
        p1_text = self.font_small.render(p1, 1, self.blue)
        p1_pos = SCREEN_W >> 3, self.p1.paddle.centery
        p1_rect = p1_text.get_rect(center = p1_pos)
        self.surface.blit(p1_text, p1_rect)

        p2 = "Player 2"
        p2_text = self.font_small.render(p2, 1, self.red)
        p2_pos = SCREEN_W - (SCREEN_W >> 3), self.p2.paddle.centery
        p2_rect = p2_text.get_rect(center = p2_pos)
        self.surface.blit(p2_text, p2_rect)

        info = "Player1 may use either keys in single-player games."
        info_text = self.font_small.render(info, 1, self.fg_color)
        info_pos = SCREEN_W >> 1, SCREEN_H - (SCREEN_H >> 3)
        info_rect = info_text.get_rect(center = info_pos)
        self.surface.blit(info_text, info_rect)

        cont = "Press any button to continue"
        cont_text = self.font_small.render(cont, 1, self.fg_color)
        cont_pos = SCREEN_W >> 1, SCREEN_H
        cont_rect = cont_text.get_rect(midbottom = cont_pos)
        self.surface.blit(cont_text, cont_rect)

    def draw_help_menu(self):
        self.draw_background()
        self.draw_paddles(True)
        self.draw_help_arrows()
        self.draw_help_text()

    def draw_paused_screen(self):
        self.draw_background()

        paused = "Paused"
        paused_text = self.font.render(paused, 1, self.fg_color)
        paused_pos = SCREEN_W >> 1, SCREEN_H >> 1
        paused_rect = paused_text.get_rect(center = paused_pos)
        self.surface.blit(paused_text, paused_rect)

        self.draw_paddles()

    def draw_win_screen(self):
        self.draw_background()

        if self.p1.winner:
            pwinner = "Player 1 wins!"
            pcolor = self.p1.color
            ppaddle = self.p1.paddle
        else:
            pwinner = "Player 2 wins!"
            pcolor = self.p2.color
            ppaddle = self.p2.paddle

        pwinner_text = self.font.render(pwinner, 1, pcolor)
        pwinner_pos = SCREEN_W >> 1, SCREEN_H >> 2
        pwinner_rect = pwinner_text.get_rect(center = pwinner_pos)
        self.surface.blit(pwinner_text, pwinner_rect)

        cont = "Press any button to continue"
        cont_text = self.font_small.render(cont, 1, self.fg_color)
        cont_pos = SCREEN_W >> 1, SCREEN_H - (SCREEN_H >> 2)
        cont_rect = cont_text.get_rect(center = cont_pos)
        self.surface.blit(cont_text, cont_rect)

        ppaddle.center = SCREEN_W >> 1, SCREEN_H >> 1
        pygame.draw.rect(self.surface, pcolor, ppaddle)

    def draw_frame(self):
        if self.show_help_menu:
            self.draw_help_menu()
        elif self.show_menu and not self.show_help_menu:
            self.draw_menu()
        elif self.paused:
            self.draw_paused_screen()
        elif self.show_win_screen:
            self.draw_win_screen()
        else:
            self.draw_game()

    def update_frame(self):
        pygame.display.flip()