import pygame
from enum import Enum
from collections import namedtuple
white = (255, 255, 255)
BLOCK_SIZE=20
Point=namedtuple('Point','x,y')
class Direction(Enum):
    RIGHT=1
    LEFT=2
    UP=3
    DOWN=4
class SnakeGame():
    def __init__(self,w=800,h=600):
        w=800
        h=600

        # display.fill(white)
        display=pygame.display.set_mode((w,h))
        pygame.display.set_caption('Snake_Game')
        snake_icon=pygame.image.load('snake.png')
        pygame.display.set_icon(snake_icon)
        self_clock=pygame.time.Clock()
        self.direction=Direction.RIGHT
        self.head=Point(self.w/2, self.h/2)
        self.snake=[self.head,
                    Point(self.head.x-BLOCK_SIZE,self.head.y),
        Point(self.head.x-(2*BLOCK_SIZE),self.head.y)]
    def UI(self):
        self.display.fill(white)
        pygame.display.flip()

    def Play_Step(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.direction=Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key==pygame.K_UP:
                    self.direction=Direction.UP
                elif event.key==pygame.K_DOWN:
                    self.direction=Direction.DOWN
    def move(self,Direction):
        x=self.head.x
        y=self.head.y
        if direction == Direction.RIGHT:
            x+=BLOCK_SIZE
        elif direction == Direction.LEFT:
            x-=BLOCK_SIZE
        elif direction == Direction.UP:
            y-= BLOCK_SIZE
        elif direction== Direction.DOWN:
            y+=BLOCK_SIZE

        self.head=Point(x,y)
if __name__ == '__main__':
    while True:
        SnakeGame()