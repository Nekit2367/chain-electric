import pygame

GRID_COLOR = (25, 25, 25)

class Grid():
    def __init__(self, width, height, targetDistance):
        self.width = width
        self.height = height
        self.targetDistance = targetDistance

        self.InitRows()
        self.InitColumns()

        self.SetPosition(0, 0)
        self.SetColor(GRID_COLOR)

        self.hovered = False
        self.pressed = False

    def InitRows(self):
        self.numberRows = int(self.height / self.targetDistance) + 1
        self.distanceRows = (self.height - 1) / (self.numberRows - 1)

    def InitColumns(self):
        self.numberColumns = int(self.width / self.targetDistance) + 1
        self.distanceColumns = (self.width - 1) / (self.numberColumns - 1)

    def SetPosition(self, x, y):
        self.x = x
        self.y = y

    def SetColor(self, color):
        self.color = color

    def Render(self, screen):
        for i in range(self.numberRows):
            x = self.x
            y = self.y + (i * self.distanceRows)
            pygame.draw.line(screen, self.color, (x, y), (x + self.width - 1, y))

        for j in range(self.numberColumns):
            x = self.x + (j * self.distanceColumns)
            y = self.y
            pygame.draw.line(screen, self.color, (x, y), (x, y + self.height - 1))

    def GetNumberRows(self):
        return self.numberRows
    
    def GetNumberColumns(self):
        return self.numberColumns
    
    def GetDistanceRows(self):
        return self.distanceRows
    
    def GetDistanceColumns(self):
        return self.distanceColumns
    
    def GetPositionX(self):
        return self.x
    
    def GetPositionY(self):
        return self.y