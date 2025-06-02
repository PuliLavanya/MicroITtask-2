import random

class SnakeEnv:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.reset()

    def reset(self):
        self.snake = [(self.grid_size // 2, self.grid_size // 2)]
        self.direction = (0, 1)  # initially moving right
        self.spawn_food()
        self.done = False
        self.score = 0
        return self.get_state()

    def spawn_food(self):
        while True:
            self.food = (random.randint(0, self.grid_size - 1),
                         random.randint(0, self.grid_size - 1))
            if self.food not in self.snake:
                break

    def get_state(self):
        head = self.snake[0]
        return (head, self.food, self.direction)

    def step(self, action):
        if self.done:
            return self.get_state(), 0, True

        # action: 0=straight, 1=right turn, 2=left turn
        self.update_direction(action)
        new_head = (self.snake[0][0] + self.direction[0],
                    self.snake[0][1] + self.direction[1])

        # Check collisions
        if (new_head in self.snake or
            not (0 <= new_head[0] < self.grid_size) or
            not (0 <= new_head[1] < self.grid_size)):
            self.done = True
            reward = -10
            return self.get_state(), reward, True

        self.snake.insert(0, new_head)

        reward = 0
        if new_head == self.food:
            reward = 10
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()  # move forward

        return self.get_state(), reward, self.done

    def update_direction(self, action):
        # Directions as vectors: up, right, down, left
        directions = [( -1, 0), (0, 1), (1, 0), (0, -1)]
        idx = directions.index(self.direction)
        if action == 1:  # turn right
            idx = (idx + 1) % 4
        elif action == 2:  # turn left
            idx = (idx - 1) % 4
        self.direction = directions[idx]
