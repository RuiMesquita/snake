import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class Button(object):
    def __init__(self, position):
        self.position = position
        self.color = (255, 0, 0)
        self.width, self.height = 300, 50
        self.font = pygame.font.Font("freesansbold.ttf", 20)
    
    def draw(self, label):
        rect = pygame.Rect(self.position, (self.width, self.height))
        text = self.font.render(label, 1, (0, 0, 0))
        pygame.draw.rect(screen, self.color, rect)
        rect.blit(text, 20, 20)
        
    def blink(self):
        pass
    

button_sp = Button((20, 20))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

running = True
while running:
    button_sp.draw("SinglePlayer")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    pygame.display.update()

pygame.quit()
