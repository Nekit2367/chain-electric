import pygame

SLIDER_BACKGROUND_COLOR = (10, 10, 10)
SLIDER_HANDLE_DEFAULT_COLOR = (150, 150, 150)
SLIDER_HANDLE_HOVERED_COLOR = (120, 120, 120)
SLIDER_HANDLE_PRESSED_COLOR = (100, 100, 100)

class Slider():
    def __init__(self, width, height, minValue, maxValue, defaultValue):
        self.width = width
        self.height = height
        self.minValue = minValue
        self.maxValue = maxValue

        self.x = 0
        self.y = 0

        self.backgroundColor = SLIDER_BACKGROUND_COLOR
        self.handleColor = SLIDER_HANDLE_DEFAULT_COLOR
        
        self.SetHandleWidth(width)
        self.handlePoint = self.handleWidth / 2

        self.value = defaultValue
        self.handleX = self.CalculateHandlePosition()

        self.hovered = False
        self.pressed = False

    def GetValue(self):
        return self.value
    
    def SetHandleWidth(self, handleWidth):
        self.handleWidth = 0.05 * handleWidth

    def CalculateHandlePosition(self):
        valueRange = self.maxValue - self.minValue
        deltaWidth = self.width - self.handleWidth
        handleX = (self.value - self.minValue) / valueRange * deltaWidth + self.handlePoint
        return handleX

    def CalculateValue(self):
        valueRange = self.maxValue - self.minValue
        deltaWidth = self.width - self.handleWidth
        value = self.minValue + ((self.handleX - self.handlePoint) / deltaWidth) * valueRange
        return value

    def SliderRestrictions(self):
        if (self.handleX - self.handlePoint < 0):
            return self.handlePoint
        
        if (self.handleX + self.handlePoint > self.width):
            return self.width - self.handlePoint

        return self.handleX
            
    def CheckBoundaries(self, x, y):
        if (x < self.x or x > self.x + self.width):
            return False
        
        if (y < self.y or y > self.y + self.height):
            return False
        
        return True

    def ProcessEvents(self, event):
        mouse = pygame.mouse
        mouseX = mouse.get_pos()[0]
        mouseY = mouse.get_pos()[1]

        if (self.CheckBoundaries(mouseX, mouseY)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.pressed = True
            else:
                self.hovered = True

        if (event.type == pygame.MOUSEBUTTONUP):
            self.pressed = False

        if (self.pressed):
            self.handleX = mouseX - self.x
            self.handleX = self.SliderRestrictions()
            self.handleColor = SLIDER_HANDLE_PRESSED_COLOR

        elif (self.hovered):
            self.handleColor = SLIDER_HANDLE_HOVERED_COLOR
            self.hovered = False

        else:
            self.handleColor = SLIDER_HANDLE_DEFAULT_COLOR

    def Update(self):
        self.value = self.CalculateValue()

    def Render(self, screen, x, y):
        self.x = x
        self.y = y

        self.Update()

        pygame.draw.rect(screen, self.backgroundColor, (x, y, self.width, self.height))

        pygame.draw.rect(screen, self.handleColor, (x + self.handleX - self.handlePoint, y, self.handleWidth, self.height))