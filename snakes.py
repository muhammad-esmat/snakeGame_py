import curses as curses

class snake:
    def __init__(self, coordinates, skin, direction = "right"):
        initBody = [
            (coordinates[0], coordinates[1]-2),
            (coordinates[0], coordinates[1]-1),
            (coordinates[0], coordinates[1])
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

    def addHead(self, steps = 1):
        snake_head = self.head

        if self.direction == "right":
            self.snakeBody.append((snake_head[0], snake_head[1]+steps))
        elif self.direction == "left":
            self.snakeBody.append((snake_head[0], snake_head[1]-steps))
        elif self.direction == "up":
            self.snakeBody.append((snake_head[0]-steps, snake_head[1]))
        elif self.direction  == "down":
            self.snakeBody.append((snake_head[0]+steps, snake_head[1]))

        self.head = self.snakeBody[-1]


    def popTail(self):
        tail = self.snakeBody.pop(0)
        self.tail = self.snakeBody[0]
        return tail

    def get_score(self):
        return str(len(self.snakeBody) - 3)

    def loser(self, mid, window):
        score = self.get_score()

        window.clear()
        window.timeout(-1)

        window.addstr(mid[0], mid[1], f"Score: {score}")

        window.getch()

