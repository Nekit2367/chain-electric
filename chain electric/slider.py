import pygame

class Slider():
    def __init__(self, width, height, minValue, maxValue, defaultValue):
        self.width = width
        self.height = height
        self.minValue = minValue
        self.maxValue = maxValue

        self.backgroundColor = (80, 80, 80)
        self.handleColor = (255, 255, 255)
        self.handleWidth = 0.1 * width
        self.handlePoint = self.handleWidth / 2

        self.value = defaultValue
        self.handleX = self.CalculateHandlePosition()

        self.hovered = False
        self.pressed = False

    def CalculateHandlePosition(self):
        valueRange = self.maxValue - self.minValue
        deltaWidth = self.width - self.handleWidth
        return (self.value - self.minValue) / valueRange * deltaWidth + self.handlePoint

    def CalculateValue(self):
        valueRange = self.maxValue - self.minValue
        deltaWidth = self.width - self.handleWidth
        return self.minValue + ((self.handleX - self.handlePoint) / deltaWidth) * valueRange
    
    def GetValue(self):
        return self.value

    def Update(self):
        mouse = pygame.mouse

        mouseX = mouse.get_pos()[0]
        mouseY = mouse.get_pos()[1]
        
        self.handleX = mouseX - self.x

        self.value = self.CalculateValue()
            
    def Render(self, screen, x, y):
        self.x = x
        self.y = y

        self.Update()

        pygame.draw.rect(screen, self.backgroundColor, (x, y, self.width, self.height))

        pygame.draw.rect(screen, self.handleColor, (x + self.handleX - self.handlePoint, y, self.handleWidth, self.height))
