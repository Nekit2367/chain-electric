from window import Window
from grid import Grid

import pygame

pygame.init()

window = Window("Chain Electric", 1280, 720, 60)

grid = Grid(window.GetWidth(), window.GetHeight(), 80)

running = True
while running:
    window.CallDelay()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.ClearScreen((0, 0, 0))

    grid.Render(window.GetScreen())

    pygame.display.flip()