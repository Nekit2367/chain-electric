from window import Window
import pygame

pygame.init()

window = Window("Chain Electric", 1280, 720, 60)

running = True
while running:
    window.CallDelay()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.ClearScreen((0, 0, 0))

    pygame.display.flip()