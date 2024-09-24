import pygame
from enum import Enum
from collections import namedtuple

white = (255, 255, 255)
BLOCK_SIZE = 20
Point = namedtuple('Point', 'x,y')

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class SnakeGame:
    def __init__(self, w=800, h=600):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((w, h))
        pygame.display.set_caption('Snake_Game')
        snake_icon = pygame.image.load('snake.png')
        pygame.display.set_icon(snake_icon)
        self.clock = pygame.time.Clock()
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]

    def UI(self):
        self.display.fill(white)

        # Draw the snake
        for segment in self.snake:
            pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(segment.x, segment.y, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()

    def Play_Step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN

    def move(self):
        x, y = self.head.x, self.head.y

        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE

        self.head = Point(x, y)

        # Update the entire snake body
        self.snake.insert(0, self.head)  # Add a new head
        if len(self.snake) > 3:  # Remove the last segment
            self.snake.pop()

if __name__ == '__main__':
    game = SnakeGame()

    while True:
        game.UI()
        game.Play_Step()
        game.move()

        game.clock.tick(10)  # Adjust the frames per second (FPS)
