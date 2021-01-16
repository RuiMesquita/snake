import pygame as pg
import random

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

GRID_SIZE = 40
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake(object):
    def __init__(self):
        self.x, self.y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        self.color = (0, 0, 255)
        self.width = GRID_SIZE
        self.height = GRID_SIZE

    def turn(self):
        pass

    def move(self):
        pass

    def get_head_position(self):
        return (self.x, self.y)

    def draw(self):
        pg.draw.rect(window, self.color, (int(self.x), int(self.y), self.width, self.height), 0)


class Food(object):
    def __init__(self):
        self.x, self.y = (0, 0)
        self.color = (255, 0, 0)
        self.x, self.y = self.randomize_position()

    def randomize_position(self):
        self.x = random.randint(0, GRID_WIDTH) * GRID_SIZE
        self.y = random.randint(0, GRID_HEIGHT) * GRID_SIZE
        return (self.x, self.y)
    
    def draw(self):
        shape = pg.Rect((int(self.x), int(self.y)), (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(window, self.color, shape)


def draw_grid(surface):
    """
    Draw a grid with two diferent colors on the game window 
    """
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                square = pg.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pg.draw.rect(surface, (255, 195, 0), square)
            else:
                square = pg.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pg.draw.rect(surface, (218, 247, 166), square)
            



snake = Snake()
food = Food()

pg.init()
pg.display.set_caption("Snake Game")
clock = pg.time.Clock()
running = True
window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
draw_grid(window)

while running:
    clock.tick(10)
    draw_grid(window)
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                pass
            elif event.key == pg.K_DOWN:
                pass
            elif event.key == pg.K_LEFT:
                pass
            elif event.key == pg.K_RIGHT:
                pass
        
    snake.draw()
    food.draw()
    pg.display.update()

pg.quit()

