from collections import deque

class snake:
    def __init__(self, coordinates, direction = "right"):
        self.initalBody = [
            [coordinates[1], coordinates[0]],
            [coordinates[1], coordinates[0]-1],
            [coordinates[1], coordinates[0]-2]
        ]

        self.snakeBody = deque(self.initalBody)

        self.direction = direction

    def move(self, steps = 1, direction = self.direction, eating = False):
        snake_head = self.snakeBody[-1]
        
        if direction == "right":
            self.snakeBody.append([snake_head[0], snake_head[1]+steps])
        elif direction == "left":
            self.snakeBody.append([snake_head[0], snake_head[1]-steps])
        elif direction == "up":
            self.snakeBody.append([snake_head[0]-steps, snake_head[1]])
        elif direction == "down":
            self.snakeBody.append([snake_head[0]+steps, snake_head[1]])
        
        if not eating:
            self.snakeBody.popleft()
