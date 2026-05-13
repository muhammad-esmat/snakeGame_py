import curses as curses
import random
from snakes import snake

screen = curses.initscr()

scr_y, scr_x = screen.getmaxyx()

window = curses.newwin(scr_y, scr_x, 0, 0)

curses.curs_set(0)

window.keypad(1)

window.timeout(100)

mid = [scr_y // 2, scr_x // 2]

food = (mid[0], mid[1])

window.addch(food[0], food[1], curses.ACS_STERLING)

player = snake([scr_y // 2, scr_x // 4], curses.ACS_BOARD)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()

    if (
        next_key == -1
        or player.line_of_motion() == "Vertical"
        and next_key in [curses.KEY_UP, curses.KEY_DOWN]
        or player.line_of_motion() == "Horizontal"
        and next_key in [curses.KEY_RIGHT, curses.KEY_LEFT]
    ):
        pass
    else:
        key = next_key

        if key == curses.KEY_UP:
            player.direction = "up"
        elif key == curses.KEY_DOWN:
            player.direction = "down"
        elif key == curses.KEY_RIGHT:
            player.direction = "right"
        elif key == curses.KEY_LEFT:
            player.direction = "left"

    player.addHead()

    if player.head == food:
        food = None
        while food is None:
            new_food = (random.randint(2, scr_y - 2), random.randint(2, scr_x - 2))
            food = new_food if not player.collides_with(food) else None
        window.addch(food[0], food[1], curses.ACS_STERLING)
    else:
        tail = player.popTail()
        window.addch(tail[0], tail[1], " ")

    if (
        player.head[0] in [1, scr_y - 1]
        or player.head[1] in [1, scr_x - 1]
        or player.head in player.snakeBody[:-1]
    ):
        player.loser(mid, window, screen)
        quit()

    window.addch(player.head[0], player.head[1], player.skin)
