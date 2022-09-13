import pong as p

from pygame import event as ev


def main():
    pong = p.Pong()
    pong.set_window_properties()

    while 1:
        for event in ev.get():
            pong.handle(event)

        #pong.update_ball_position()

        pong.draw_background()
        pong.draw_center_line()
        pong.draw_ball()
        pong.draw_scores()
        pong.draw_paddles()
        pong.update_frame()

if __name__ == "__main__":
    main()