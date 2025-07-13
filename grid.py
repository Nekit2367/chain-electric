from matrix import Vertex
from matrix import Matrix

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
    
    def GetMatrix(self) -> Matrix:
        n = self.GetNumberRows()
        m = self.GetNumberColumns()

        matrix = Matrix(n, m)

        for i in range(n):
            for j in range(m):
                vertex = Vertex(i * self.distanceRows, j * self.distanceColumns)
                matrix.SetVertex(vertex, i, j)

        return matrix
    
    def CheckBoundaries(self):
        if (pygame.mouse.get_pos()[0] < self.x or pygame.mouse.get_pos()[0] > self.x + self.width):
            return False
        
        if (pygame.mouse.get_pos()[1] < self.y or pygame.mouse.get_pos()[1] > self.y + self.height):
            return False
        
        return True

    def GetNearVertex(self) -> Vertex:
        mouse = pygame.mouse
        mouseX = mouse.get_pos()[0] - self.x
        mouseY = mouse.get_pos()[1] - self.y

        column = round(mouseX / self.GetDistanceColumns())
        row = round(mouseY / self.GetDistanceRows())

        if (column <= self.GetNumberColumns() and row <= self.GetDistanceRows()):
            matrix = self.GetMatrix()
            return matrix.GetVertexes()[row][column]
        
        return Vertex()