from window import Window
from grid import Grid
from slider import Slider
from button import Button

import pygame

pygame.init()

window = Window("Electrical Circuit Simulator", 1280, 720, 60)

grid = Grid(window.GetWidth() - 215, window.GetHeight() - 10, 25)
grid.SetPosition(5, 5)

sliderFirst = Slider(200, 20, 0, 100, 10)
sliderSecond = Slider(200, 20, 0, 100, 10)
sliderThird = Slider(200, 20, 0, 100, 10)

buttonFirst = Button(200, 20, "Button")
buttonSecond = Button(200, 20, "Button")

running = True
while running:
    window.CallDelay()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            sliderFirst.ProcessEvents(event)
            sliderSecond.ProcessEvents(event)
            sliderThird.ProcessEvents(event)

    buttonFirst.ProcessEvent()
    buttonSecond.ProcessEvent()

    window.ClearScreen((0, 0, 0))

    grid.Render(window.GetScreen())

    sliderFirst.Render(window.GetScreen(), window.GetWidth() - 205, 5)
    sliderSecond.Render(window.GetScreen(), window.GetWidth() - 205, 30)
    sliderThird.Render(window.GetScreen(), window.GetWidth() - 205, 55)

    buttonFirst.Render(window.GetScreen(), window.GetWidth() - 205, 80)
    if (buttonFirst.GetValue()):
        print("First")

    buttonSecond.Render(window.GetScreen(), window.GetWidth() - 205, 105)
    if (buttonSecond.GetValue()):
        print("Second")

    pygame.display.flip()