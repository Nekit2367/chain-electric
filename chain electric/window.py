import pygame

class Window():
    def __init__(self, title, width, height, fps):
        self.title = title
        self.width = width
        self.height = height
        self.fps = fps

        self.SetScreenResolution()
        self.SetClock()

    def GetTitle(self):
        return self.title

    def GetWidth(self):
        return self.width
    
    def GetHeight(self):
        return self.height
    
    def GetFPS(self):
        return self.fps
    
    def GetScreen(self):
        return self.screen

    def SetScreenResolution(self):
        self.screen = pygame.display.set_mode((self.width, self.height))

    def SetClock(self):
        self.clock = pygame.time.Clock()

    def CallDelay(self):
        self.clock.tick(self.fps)

    def ClearScreen(self, color):
        self.screen.fill(color)