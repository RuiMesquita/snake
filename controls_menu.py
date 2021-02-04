import pygame


def controls_menu():

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600


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


    def text_to_screen(font, surface, message, x_pos = 400, y_pos = 200):
        """
        prints and centers text on the screen
        """
        text = font.render(message, 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x_pos, y_pos)
        surface.blit(text, text_rect)


    button_back = Button((SCREEN_WIDTH/2 - 150, 500), "Back")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((218, 247, 166))
    pygame.display.set_caption("Controls")

    font = pygame.font.Font("freesansbold.ttf", 30)
    label_font = pygame.font.Font("freesansbold.ttf", 20)

    running = True
    while running:
        screen.fill((218, 247, 166))
        button_back.draw(label_font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            
            # keep track of the cursor position
            pos = pygame.mouse.get_pos()

            # keep track if the mouse is inside a button when pressed 
            if event.type == pygame.MOUSEBUTTONUP:
                if button_back.collision_point(pos):
                    running = False
                    return "back"

            # Creating the hover effect by checking the mouse position
            elif button_back.collision_point(pos):
                button_back.hovered = True

            else:
                button_back.hovered = False
        
        text_to_screen(font, screen, "turn up - up arrow key")
        text_to_screen(font, screen, "turn down - down arrow key", y_pos=250)
        text_to_screen(font, screen, "turn right - right arrow key", y_pos=300)
        text_to_screen(font, screen, "turn left - left arrow key", y_pos=350)
        text_to_screen(font, screen, "pause - esc", y_pos=400)

        pygame.display.update()
