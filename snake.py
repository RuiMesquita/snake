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
        self.positions = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.color = (0, 0, 255)
        self.width = GRID_SIZE
        self.height = GRID_SIZE

        self.length = 1
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def turn(self, direction):
        if self.length > 1 and (direction[0] * -1, direction[1] * -1) == self.direction:
            pass
        else:
            self.direction = direction

    def move(self):
        current_pos = self.get_head_position()
        x, y = self.direction
        new_pos = (((current_pos[0] + (x * GRID_SIZE))), (current_pos[1] + (y * GRID_SIZE)))

        if self.length > 2 and new_pos in self.positions:
            lose_screen()
            self.reset()
        else:
            self.positions.insert(0, new_pos)
            if len(self.positions) > self.length:
                self.positions.pop()
            
    def get_head_position(self):
        return self.positions[0]

    def reset(self):
        self.positions = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.length = 1
        self.score = 0
        food.randomize_position()

    def draw(self):
        for position in self.positions:
            pg.draw.rect(window, self.color, (int(position[0]), int(position[1]), self.width, self.height), 0)


class Food(object):
    def __init__(self):
        self.x, self.y = (0, 0)
        self.color = (255, 0, 0)
        self.x, self.y = self.randomize_position()

    def randomize_position(self):
        self.x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        self.y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        return (self.x, self.y)
    
    def draw(self):
        shape = pg.Rect((int(self.x), int(self.y)), (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(window, self.color, shape)
    
    def get_position(self):
        return (self.x, self.y)


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


def lose_screen():
    """
    Shows a lose screen and waits for the user to restart the game
    """
    display_message_in_white("Press R to restart the game")
    paused = True
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit() 

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    paused = False


def text_objects(text, font):
    """
    Print text to a surface
    """
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect() 


def display_message_in_white(message):
    """
    Displays a message to the screen in a white box
    """
    large_text = pg.font.SysFont("Arial", 20)
    MENU_WIDTH, MENU_HEIGHT = 400, 200
    shape = (SCREEN_WIDTH / 2 - (MENU_WIDTH / 2), SCREEN_HEIGHT / 2 - (MENU_HEIGHT / 2), MENU_WIDTH, MENU_HEIGHT)

    pg.draw.rect(window, (255, 255, 255), shape, 0)
    pg.draw.rect(window, (0, 0, 0), shape, 2)

    text_surf, text_rect = text_objects(message, large_text)
    text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    window.blit(text_surf, text_rect)

    pg.display.update()


def pause_game():
    """
    Introduces a infinite loop in the in order to pause the game
    """
    display_message_in_white("Press ESC to resume")
    paused = True
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit() 

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    paused = False

snake = Snake()
food = Food()

pg.init()
pg.display.set_caption("Snake Game")

font = pg.font.Font("freesansbold.ttf", 17)

clock = pg.time.Clock()
running = True
window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
draw_grid(window)

while running:
    clock.tick(10)
    draw_grid(window)
    pg.display.flip()

    snake.move()

    if snake.get_head_position() == food.get_position():
        food.randomize_position()
        snake.score += 1
        snake.length += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake.turn(UP)
            elif event.key == pg.K_DOWN:
                snake.turn(DOWN)
            elif event.key == pg.K_LEFT:
                snake.turn(LEFT)
            elif event.key == pg.K_RIGHT:
                snake.turn(RIGHT)
            elif event.key == pg.K_ESCAPE:
                pause_game()
        
    snake.draw()
    food.draw()
    text = font.render(f"Score: {snake.score}", 1, (0, 0, 0))
    window.blit(text, (5, 10))
    pg.display.update()

pg.quit()
