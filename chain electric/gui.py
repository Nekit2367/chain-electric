from window import Window
import pygame

class Grid():
    def __init__(self, window : Window, width, height):
        self.window = window
        self.width = width
        self.height = height

        self.color = (255, 255, 255)

    def SetColor(self, color):
        self.color = color

    def Render(self, screen):
        for i in range(10):
            x = i * self.width
            pygame.draw.line(screen, self.color, (x, 0), (x, self.window.GetHeight()))

        for i in range(10):
            y = i * self.height
            pygame.draw.line(screen, self.color, (0, y), (self.window.GetWidth(), y))

class Button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = (0, 0, 0)

    def SetColor(self, color):
        self.color = color

    def Render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))