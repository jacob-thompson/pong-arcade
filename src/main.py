import pong as p

from pygame import event

def main():
    pong = p.Pong()

    pong.set_window_properties()
    pong.print_help_info()

    frame_rate = 60

    while 1:
        for e in event.get():
            pong.handle(e)

        pong.tick(frame_rate)

        if pong.show_menu == False:
            pong.update_paddle_position()
            pong.update_ball_position()

        pong.draw_frame()
        pong.update_frame()

if __name__ == "__main__":
    main()