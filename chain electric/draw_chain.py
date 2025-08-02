import pygame as pg
# цвета
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
brown=(79, 70,0)
grey=(128,128,128)
# 
pg.font.init()
font_style = pg.font.SysFont("bahnschrift", 30) 
def draw_fon(font_style,screen,massive_buttons,event):
    # добавить конденсатор
    value = font_style.render('конденсатор', True, black)
    screen.blit(value, [1100, 660])
    # добавить катушку
    value = font_style.render('катушка', True, black)
    screen.blit(value, [1100, 780])
    # добавить резистор
    value = font_style.render('резистор', True, black)
    screen.blit(value, [1100, 540])
    # добавить напряжение
    value = font_style.render('напряжение', True, black)
    screen.blit(value, [1100, 420])
    # добавить провод
    value = font_style.render('провод', True, black)
    screen.blit(value, [1125, 240])
    # добавить клюс
    value = font_style.render('ключ', True, black)
    screen.blit(value, [1125, 320])
    # добавить диод
    value = font_style.render('диод', True, black)
    screen.blit(value, [1125, 160])
    # добавить лампочку
    value = font_style.render('лампочка', True, black)
    screen.blit(value, [1125, 80])
    # кнопки
    for button in massive_buttons:
        button.draw(screen)
        button.ProcessEvents(event)
