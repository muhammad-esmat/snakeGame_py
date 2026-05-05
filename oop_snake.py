from collections import deque
import curses

class snake:
    def __init__(self, coordinates, direction = "right"):
        self.initalBody = [
            [coordinates[1], coordinates[0]-2],
            [coordinates[1], coordinates[0]-1],
            [coordinates[1], coordinates[0]]
        ]

        self.snakeBody = deque(self.initalBody)

        self.direction = direction

        self.skin = curses.ACS_DIAMOND

        self.head = self.snakeBody[-1]

    
    def line_of_motion(self):
        LOM = "Horizontal"

        if self.head[1] != self.snakeBody[-2][1]:
            LOM = "Vertical"

        return LOM

    def move(self, direction = "", steps = 1, eating = False):
        snakeLOM = self.line_of_motion()

        snake_head = self.head
        
        if snakeLOM == "right":
            self.snakeBody.append([snake_head[0], snake_head[1]+steps])
        elif direction == "left":
            self.snakeBody.append([snake_head[0], snake_head[1]-steps])
        elif direction == "up":
            self.snakeBody.append([snake_head[0]-steps, snake_head[1]])
        elif direction  == "down":
            self.snakeBody.append([snake_head[0]+steps, snake_head[1]])
        
        if not eating:
            self.snakeBody.popleft()

        self.head = self.snakeBody[-1]
    
    def get_score(self):
        return len(self.snakeBody)


    def loser(self, mid, window):
        score = self.get_score()

        window.clear()
        window.timeout(-1)

        window.addstr(mid[0], mid[1], score)

        window.getch()
