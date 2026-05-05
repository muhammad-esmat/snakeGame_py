from collections import deque
import curses

class snake:
    def __init__(self, coordinates, direction = "right"):
        initBody = [
            (coordinates[0], coordinates[1]-2),
            (coordinates[0], coordinates[1]-1),
            (coordinates[0], coordinates[1])
        ]
        
        self.headless_body = set(initBody[0:2])

        self.queueBody = deque(initBody)

        self.direction = direction

        self.skin = curses.ACS_DIAMOND

        self.head = self.queueBody[-1]
        self.tail = self.queueBody[0]
        self.size = 3

    
    def line_of_motion(self):
        LOM = "Horizontal"

        if self.head[0] != self.queueBody[-2][0]:
            LOM = "Vertical"

        return LOM

    def collides_with(self, object):
        if (object == self.head or object in self.headless_body):
            return True
        else:
            return False

    def addHead(self, foodPos, steps = 1):
        snake_head = self.head

        if self.direction == "right":
            self.queueBody.append((snake_head[0], snake_head[1]+steps))
        elif self.direction == "left":
            self.queueBody.append((snake_head[0], snake_head[1]-steps))
        elif self.direction == "up":
            self.queueBody.append((snake_head[0]-steps, snake_head[1]))
        elif self.direction  == "down":
            self.queueBody.append((snake_head[0]+steps, snake_head[1]))

        self.head = self.queueBody[-1]
        if self.head in self.headless_body:
            return 

        self.headless_body.add(self.queueBody[-2])

        self.size += 1

    def popTail(self):
        tail = self.queueBody.popleft()
        self.headless_body.remove(tail)
        self.tail = self.queueBody[0]
        return tail

    def get_score(self):
        return str(len(self.queueBody))

    def loser(self, mid, window):
        score = self.get_score()

        window.clear()
        window.timeout(-1)

        window.addstr(mid[0], mid[1], f"Score: {score}")

        window.getch()

