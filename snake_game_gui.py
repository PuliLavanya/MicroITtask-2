import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)

        if new_head in self.positions[1:]:
            return False  # collided with itself

        self.positions.insert(0, new_head)
        return True

    def grow(self):
        # Don't remove tail so snake grows
        pass

    def trim(self):
        self.positions.pop()

    def change_direction(self, new_dir):
        # Prevent reverse direction
        opposite = (-self.direction[0], -self.direction[1])
        if new_dir != opposite:
            self.direction = new_dir

class Food:
    def __init__(self, snake_positions):
        self.position = self.spawn(snake_positions)

    def spawn(self, snake_positions):
        positions = [(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if (x,y) not in snake_positions]
        return random.choice(positions)

def draw_rect(color, position):
    rect = pygame.Rect(position[0]*CELL_SIZE, position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def main():
    snake = Snake()
    food = Food(snake.positions)
    running = True
    score = 0

    while running:
        clock.tick(10)  # FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        moved = snake.move()
        if not moved:
            print(f"Game Over! Your score: {score}")
            running = False
            continue

        if snake.positions[0] == food.position:
            score += 1
            food = Food(snake.positions)
            snake.grow()
        else:
            snake.trim()

        # Draw everything
        screen.fill(BLACK)
        draw_rect(RED, food.position)
        for pos in snake.positions:
            draw_rect(GREEN, pos)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
