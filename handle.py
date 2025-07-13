from matrix import Vertex
from grid import Grid
import pygame

HANDLE_COLOR = (200, 200, 200)

class Handle():
    def __init__(self, grid : Grid):
        self.grid = grid

        self.hovered = False
        self.pressed = False

        self.elementBegin = Vertex()
        self.elementEnd = Vertex()

    def Place(self):
        mouse = pygame.mouse
        mousePressed = mouse.get_pressed()[0]

        self.hovered = self.grid.CheckBoundaries()

        if not self.pressed and self.hovered and mousePressed:
            self.pressed = True
            self.elementBegin = self.grid.GetNearVertex()

        elif self.pressed and not mousePressed:
            self.pressed = False
            if self.hovered:
                self.elementEnd = self.grid.GetNearVertex()

    def Render(self, screen):
        ex = self.elementEnd.GetX()
        ey = self.elementEnd.GetY()

        bx = self.elementBegin.GetX()
        by = self.elementBegin.GetY()

        if (self.pressed):
            pygame.draw.line(screen, HANDLE_COLOR, (by + self.grid.y, bx + self.grid.x), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 2)
            pygame.draw.circle(screen, HANDLE_COLOR, (by + self.grid.y, bx + self.grid.x), 4)

        elif (ex != 0 and ey != 0):
            pygame.draw.line(screen, HANDLE_COLOR, (by + self.grid.y, bx + self.grid.x), (ey + self.grid.y, ex + self.grid.x))
            pygame.draw.circle(screen, HANDLE_COLOR, (by + self.grid.y, bx + self.grid.x), 4)
            pygame.draw.circle(screen, HANDLE_COLOR, (ey + self.grid.y, ex + self.grid.x), 4)