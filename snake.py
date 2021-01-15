import pygame as pg

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake(object):
    def __init__(self, color, width, height):
        self.x, self.y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        self.color = color
        self.width = width
        self.height = height

    def move(self, direction):
        pass

    def draw(self):
        pg.draw.rect(window, self.color, (int(self.x), int(self.y), self.width, self.height), 0)


class Food(object):
    pass

snake = Snake((0, 255, 0), 25, 25)

pg.init()
pg.display.set_caption("Snake Game")
clock = pg.time.Clock()
running = True
window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill((255, 255, 255))

while running:
    clock.tick(60)
    window.fill((255, 255, 255))
    pg.display.flip()

    for event in pg.event.get():
        if event.type  == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        
    snake.draw()
    pg.display.update()

pg.quit()

