import pygame

BUTTON_BACKGROUND_COLOR = (10, 10, 10)
BUTTON_TEXT_COLOR = (200, 200, 200)
BUTTON_HANDLE_HOVERED_COLOR = (100, 100, 100)
BUTTON_HANDLE_PRESSED_COLOR = (40, 10, 10)

class Button():
    def __init__(self, width, height, text):
        self.width = width
        self.height = height

        self.color = BUTTON_BACKGROUND_COLOR
        self.text = text

        self.x = 0
        self.y = 0

        self.hovered = False
        self.pressed = False
        self.value = False

        self.fontStyle = pygame.font.SysFont("Arial", int(self.height / 2)) 

    def CheckBoundaries(self, x, y):
        if (x < self.x or x > self.x + self.width):
            return False
        
        if (y < self.y or y > self.y + self.height):
            return False
        
        return True

    def ProcessEvent(self):
        mouse = pygame.mouse
        mouseX = mouse.get_pos()[0]
        mouseY = mouse.get_pos()[1]
        mousePressed = mouse.get_pressed()[0]

        self.value = False

        self.hovered = self.CheckBoundaries(mouseX, mouseY)

        if self.hovered and mousePressed:
            self.pressed = True

        elif self.pressed and not mousePressed:
            self.pressed = False
            if self.hovered:
                self.value = True

        if self.pressed:
            self.color = BUTTON_HANDLE_PRESSED_COLOR

        elif self.hovered:
            self.color = BUTTON_HANDLE_HOVERED_COLOR

        else:
            self.color = BUTTON_BACKGROUND_COLOR

    def RenderText(self, screen):
        source = self.fontStyle.render(self.text, True, BUTTON_TEXT_COLOR)
        textRect = source.get_rect()
        centeredY = self.y + (self.height - textRect.height) / 2

        screen.blit(source, [self.x + (self.width - textRect.width) / 2, centeredY])

    def Render(self, screen, x, y):
        self.x = x
        self.y = y

        pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))
        
        self.RenderText(screen)

    def GetValue(self):
        return self.value