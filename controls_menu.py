import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((218, 247, 166))
pygame.display.set_caption("Controls")

font = pygame.font.Font("freesansbold.ttf", 30)

running = True
while running:
    screen.fill((218, 247, 166))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    text = font.render(f"UP ARROW KEY -> Turn Upwards", 1, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH/2, 200)
    screen.blit(text, text_rect)
    pygame.display.update()
pygame.quit()
