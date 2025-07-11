from window import Window
from grid import Grid

import pygame

pygame.init()

window = Window("Chain Electric", 640, 480, 60)
grid = Grid(window.GetWidth(), window.GetHeight(), 80)

running = True
while running:
    window.CallDelay()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.ClearScreen((0, 0, 0))

    # Render
    grid.Render(window.GetScreen())

    pygame.display.flip()