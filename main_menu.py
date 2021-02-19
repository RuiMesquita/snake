import pygame
import sys


def main_menu():

    SCREEN_WIDTH = 450
    SCREEN_HEIGHT = 400

    class Button(object):
        def __init__(self, position, label):
            self.position = position
            self.color = (255, 195, 0)
            self.width, self.height = 300, 50
            self.label = label
            self.hovered = False
        
        def draw(self, font):
            rect = pygame.Rect(self.position, (self.width, self.height))
            pygame.draw.rect(screen, self.color, rect, 0)
            if self.hovered:
                pygame.draw.rect(screen, (255, 0, 0), rect, 2)
            else:
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)

            text_surface = font.render(self.label, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.center = (SCREEN_WIDTH / 2, self.position[1] + self.height/2)
            screen.blit(text_surface, text_rect)

        def collision_point(self, point):
            if point[0] > self.position[0] and point[0] < self.position[0] + self.width:
                if point[1] > self.position[1] and point[1] < self.position[1] + self.height:
                    return True
                else:
                    return False


    button_play = Button((SCREEN_WIDTH/2 - 150, 200), "Play")
    button_exit = Button((SCREEN_WIDTH/2 - 150, 270), "Exit")

    # Initialize pygame
    pygame.init()

    title_font = pygame.font.Font("freesansbold.ttf", 60)
    label_font = pygame.font.Font("freesansbold.ttf", 20)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((218, 247, 166))
    pygame.display.set_caption("Main Menu")

    running = True
    while running:
        button_play.draw(label_font)
        button_exit.draw(label_font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            
            # keep track of the cursor position
            pos = pygame.mouse.get_pos()

            # keep track if the mouse is inside a button when pressed 
            if event.type == pygame.MOUSEBUTTONUP:
                if button_exit.collision_point(pos):
                    running = False
                    return "exit"
                elif button_play.collision_point(pos):
                    running = False
                    return "play"

            # Creating the hover effect by checking the mouse position
            elif button_exit.collision_point(pos):
                button_exit.hovered = True
            elif button_play.collision_point(pos):
                button_play.hovered = True
            else:
                button_exit.hovered = False
                button_play.hovered = False

        title = title_font.render(f"Snake Game", 0, (255, 255, 255))
        title_centered = title.get_rect(center = (SCREEN_WIDTH/2, 80))
        screen.blit(title, title_centered)
        pygame.display.update()

    pygame.quit()
