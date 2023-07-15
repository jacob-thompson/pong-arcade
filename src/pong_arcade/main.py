from .pong import Pong

from pygame import event

def main():
    pong = Pong()

    pong.set_window_properties()
    pong.print_info()

    while 1:
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