import pygame

class Grid():
    def __init__(self, width, height, targetDistance):
        self.width = width
        self.height = height
        self.targetDistance = targetDistance

        self.color = (30, 30, 30)

        self.InitRows()
        self.InitColumns()

    def SetColor(self, color):
        self.color = color

    def InitRows(self):
        self.numberRows = int(self.height / self.targetDistance) + 1
        self.distanceRows = (self.height - 1) / (self.numberRows - 1)

    def InitColumns(self):
        self.numberColumns = int(self.width / self.targetDistance) + 1
        self.distanceColumns = (self.width - 1) / (self.numberColumns - 1)

    def Render(self, screen):
        for i in range(self.numberRows):
            y = i * self.distanceRows
            pygame.draw.line(screen, self.color, (0, y), (self.width, y))

        for j in range(self.numberColumns):
            x = j * self.distanceColumns
            pygame.draw.line(screen, self.color, (x, 0), (x, self.height))

    def GetNumberRows(self):
        return self.numberRows
    
    def GetNumberColumns(self):
        return self.numberColumns
    
    def GetDistanceRows(self):
        return self.distanceRows
    
    def GetDistanceColumns(self):
        return self.distanceColumns