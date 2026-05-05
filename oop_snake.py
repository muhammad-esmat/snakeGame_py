from collections import deque
import curses

class snake:
    def __init__(self, coordinates, direction = "right"):
        initBody = [
            (coordinates[0], coordinates[1]-2),
            (coordinates[0], coordinates[1]-1),
            (coordinates[0], coordinates[1])
        ]
        
        self.setBody = set(initBody)

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

    def move(self, mid, window, foodPos, steps = 1):
        snake_head = self.head
        player_hit_food = False

        if self.direction == "right":
            self.queueBody.append((snake_head[0], snake_head[1]+steps))
        elif self.direction == "left":
            self.queueBody.append((snake_head[0], snake_head[1]-steps))
        elif self.direction == "up":
            self.queueBody.append((snake_head[0]-steps, snake_head[1]))
        elif self.direction  == "down":
            self.queueBody.append((snake_head[0]+steps, snake_head[1]))
        
        if self.queueBody[-1] in self.setBody:
            self.loser(mid, window)

        self.head = self.queueBody[-1]
        self.setBody.add(self.head)
        window.addch(self.head[0], self.head[1], self.skin)

        if foodPos != self.head:
            window.addch(self.tail[0], self.tail[1], ' ')
            tail = self.queueBody.popleft()
            self.setBody.remove(tail)
            self.tail = self.queueBody[0]
        else:
            self.size += 1
            player_hit_food = True

        return player_hit_food
    
    def get_score(self):
        return str(len(self.queueBody))

    def loser(self, mid, window):
        score = self.get_score()

        window.clear()
        window.timeout(-1)

        window.addstr(mid[0], mid[1], f"Score: {score}")

        window.getch()

        quit()
