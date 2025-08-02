import pygame

class Window():
    def __init__(self, title, width, height, fps):
        info = pygame.display.Info()
        self.width = width
        self.height = height
        self.fps = fps

        self.SetTitle(title)
        self.SetScreenResolution()
        self.SetClock()

    def SetTitle(self, title):
        self.title = title
        pygame.display.set_caption(title)

    def SetIcon(self, path):
        icon = pygame.image.load(path)
        pygame.display.set_icon(icon)

    def SetScreenResolution(self):
        self.screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)#pygame.FULLSCREEN

    def SetClock(self):
        self.clock = pygame.time.Clock()

    def CallDelay(self):
        self.clock.tick(self.fps)

    def ClearScreen(self, color):
        self.screen.fill(color)

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