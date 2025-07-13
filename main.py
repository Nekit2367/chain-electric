from window import Window
from slider import Slider
from button import Button
from grid import Grid
from handle import Handle

import pygame

pygame.init()

window = Window("Electrical Circuit Simulator", 1280, 720, 60)

grid = Grid(window.GetWidth() - 215, window.GetHeight() - 10, 25)
grid.SetPosition(5, 5)

# matrix = grid.GetMatrix()
# matrix.Print()

handle = Handle(grid)

slider1 = Slider(200, 20, 0, 100, 10)
slider2 = Slider(200, 20, 0, 100, 10)
slider3 = Slider(200, 20, 0, 100, 10)

button1 = Button(200, 20, "Button")
button2 = Button(200, 20, "Button")

running = True
while running:
    window.CallDelay()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        else:
            slider1.ProcessEvents(event)
            slider2.ProcessEvents(event)
            slider3.ProcessEvents(event)

    button1.ProcessEvent()
    button2.ProcessEvent()

    window.ClearScreen((0, 0, 0))

    grid.Render(window.GetScreen())

    handle.Place()
    handle.Render(window.GetScreen())

    slider1.Render(window.GetScreen(), window.GetWidth() - 205, 5)
    slider2.Render(window.GetScreen(), window.GetWidth() - 205, 30)
    slider3.Render(window.GetScreen(), window.GetWidth() - 205, 55)

    button1.Render(window.GetScreen(), window.GetWidth() - 205, 80)
    button2.Render(window.GetScreen(), window.GetWidth() - 205, 105)

    pygame.display.flip()