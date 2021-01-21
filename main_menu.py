import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Button(object):
    def __init__(self, position):
        self.position = position
        self.color = (255, 195, 0)
        self.width, self.height = 300, 50
    
    def draw(self):
        rect = pygame.Rect(self.position, (self.width, self.height))
        pygame.draw.rect(screen, self.color, rect)
        
    def blink(self):
        pass
    

button_sp = Button((SCREEN_WIDTH/2 - 150, 200))
button_mp = Button((SCREEN_WIDTH/2 - 150, 300))
button_exit = Button((SCREEN_WIDTH/2 - 150, 400))

pygame.init()

title_font = pygame.font.Font("freesansbold.ttf", 60)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((218, 247, 166))
pygame.display.set_caption("Main Menu")

running = True
while running:
    button_sp.draw()
    button_mp.draw()
    button_exit.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    title = title_font.render(f"Snake Game", 0, (255, 255, 255))
    title_centered = title.get_rect(center = (SCREEN_WIDTH/2, 80))
    screen.blit(title, title_centered)
    pygame.display.update()

pygame.quit()
