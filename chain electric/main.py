from window import Window
from slider import Slider
import pygame

pygame.init()

window = Window("Chain Electric", 1280, 720, 60)
slider = Slider(300, 40, 0, 100, 10)

running = True
while running:
    window.CallDelay()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            slider.ProcessEvents(event)

    window.ClearScreen((0, 0, 0))

    slider.Render(window.GetScreen(), 100, 100)
    print(slider.GetValue())

    pygame.display.flip()