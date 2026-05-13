import curses as curses
import time


class snake:
    def __init__(self, coordinates, skin, direction="right"):
        initBody = [
            (coordinates[0], coordinates[1] - 2),
            (coordinates[0], coordinates[1] - 1),
            (coordinates[0], coordinates[1]),
        ]

        self.snakeBody = initBody

        self.direction = direction

        self.skin = skin

        self.head = self.snakeBody[-1]
        self.tail = self.snakeBody[0]

    def line_of_motion(self):
        LOM = "Horizontal"

        if self.head[0] != self.snakeBody[-2][0]:
            LOM = "Vertical"

        return LOM

    def collides_with(self, object):
        if object in self.snakeBody:
            return True
        else:
            return False

    def addHead(self, steps=1):
        snake_head = self.head

        if self.direction == "right":
            self.snakeBody.append((snake_head[0], snake_head[1] + steps))
        elif self.direction == "left":
            self.snakeBody.append((snake_head[0], snake_head[1] - steps))
        elif self.direction == "up":
            self.snakeBody.append((snake_head[0] - steps, snake_head[1]))
        elif self.direction == "down":
            self.snakeBody.append((snake_head[0] + steps, snake_head[1]))

        self.head = self.snakeBody[-1]

    def popTail(self):
        tail = self.snakeBody.pop(0)
        self.tail = self.snakeBody[0]
        return tail

    def get_score(self):
        return str(len(self.snakeBody) - 3)

    def loser(self, mid, window, screen):
        scr_y, scr_x = screen.getmaxyx()

        lose_msg1 = "Snake hit!!"
        lose_msg2 = f"Current score: {self.get_score()}"
        lose_msg3 = "Press any key to exit ..."

        curses.flushinp()
        window.erase()

        window.addstr(
            mid[0] - 2, abs(mid[1] - (len(lose_msg1) // 2)), lose_msg1, curses.A_BOLD
        )

        window.addstr(
            mid[0] + 2,
            mid[1] - (len(lose_msg2) // 2),
            lose_msg2,
        )

        window.timeout(-1)
        window.getch()
        time.sleep(1)

        curses.flushinp()
        window.erase()

        window.addstr(
            mid[0],
            mid[1] - (len(lose_msg3) // 2),
            lose_msg3,
            curses.A_BLINK,
        )

        window.timeout(-1)
        window.getch()
        time.sleep(2)
