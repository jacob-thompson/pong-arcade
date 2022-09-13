import pong as p

from pygame import event as ev

def main():
    pong = p.Pong()
    pong.set_window_properties()
    pong.print_help_info()

    while 1:
        for event in ev.get():
            pong.handle(event)

        pong.update_ball_position()

        pong.draw_frame()
        pong.update_frame()

if __name__ == "__main__":
    main()