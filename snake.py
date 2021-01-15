import pygame as pg

HEIGHT = 700
WIDTH = 1000


class Snake(object):
    def __init__(self, color, width, height):
        self.x, self.y = WIDTH/2, HEIGHT/2
        self.color = color
        self.width = width
        self.height = height

    def move(self):
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
window = pg.display.set_mode((WIDTH, HEIGHT))
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

