import pygame
black=(0,0,0)
class Knot():
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y
        self.screen=screen
    def draw_point(self):
        pygame.draw.circle(self.screen,black,(self.x,self.y),5)
class Grid():
    def __init__(self, width, height, targetDistance,screen):
        self.width = width
        self.height = height
        self.targetDistance = targetDistance

        self.InitRows()
        self.InitColumns()

        self.SetPosition(5, 75)
        self.SetColor(30, 30, 30)

        self.massive_knots=[]
        self.screen=screen

    def InitRows(self):
        self.numberRows = int(self.height / self.targetDistance) + 1
        self.distanceRows = (self.height - 1) / (self.numberRows - 1)

    def InitColumns(self):
        self.numberColumns = int(self.width / self.targetDistance) + 1
        self.distanceColumns = (self.width - 1) / (self.numberColumns - 1)

    def SetPosition(self, x, y):
        self.x = x
        self.y = y

    def SetColor(self, r, g, b):
        self.color = (r, g, b)

    def Render(self,screen):
        for i in range(self.GetNumberRows()):
            for j in range(self.GetNumberColumns()):
                x = self.x + (j * self.distanceColumns)
                y = self.y + (i * self.distanceRows)
                pygame.draw.circle(screen,black,(x,y),5)
                self.massive_knots.append(Knot(x,y,self.screen))

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
    
    def GetMassive(self):
        return self.massive_knots