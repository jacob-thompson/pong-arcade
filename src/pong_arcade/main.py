from .pong import Pong

from sys import argv

from pygame import event, quit


def main():
    lightmode = len(argv) > 1
    pong = Pong(lightmode)

    pong.set_window_properties()
    pong.print_info()

    while pong.running:
        pong.tick()

        for e in event.get():
            pong.handle_event(e)

        if pong.game_in_progress():
            pong.update_paddle_position()
            pong.update_ball_position()

        pong.draw_frame()
        pong.update_frame()


if __name__ == "__main__":
    main()
    quit()
