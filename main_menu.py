import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Button(object):
    def __init__(self, position, label):
        self.position = position
        self.color = (255, 195, 0)
        self.width, self.height = 300, 50
        self.label = label
    
    def draw(self, font):
        rect = pygame.Rect(self.position, (self.width, self.height))
        pygame.draw.rect(screen, self.color, rect, 0)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

        text_surface = font.render(self.label, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH / 2, self.position[1] + self.height/2)
        screen.blit(text_surface, text_rect)
        
    def blink(self):
        pass

button_sp = Button((SCREEN_WIDTH/2 - 150, 200), "SinglePlayer")
button_mp = Button((SCREEN_WIDTH/2 - 150, 300), "MultiPlayer")
button_exit = Button((SCREEN_WIDTH/2 - 150, 400), "Exit")

pygame.init()

title_font = pygame.font.Font("freesansbold.ttf", 60)
label_font = pygame.font.Font("freesansbold.ttf", 20)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((218, 247, 166))
pygame.display.set_caption("Main Menu")

running = True
while running:
    button_sp.draw(label_font)
    button_mp.draw(label_font)
    button_exit.draw(label_font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if button_exit.rect.collidepoint(pos):
                running = False

    title = title_font.render(f"Snake Game", 0, (255, 255, 255))
    title_centered = title.get_rect(center = (SCREEN_WIDTH/2, 80))
    screen.blit(title, title_centered)
    pygame.display.update()

pygame.quit()
