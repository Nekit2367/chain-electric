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
def draw_fon(font_style,screen,massive_buttons):
    # добавить резистор
    value = font_style.render('резистор', True, black)
    screen.blit(value, [1100, 490])
    # добавить напряжение
    value = font_style.render('напряжение', True, black)
    screen.blit(value, [1100, 370])
    # добавить провод
    value = font_style.render('провод', True, black)
    screen.blit(value, [1125, 300])
    # добавить диод
    value = font_style.render('диод', True, black)
    screen.blit(value, [1125, 200])
    # добавить лампочку
    value = font_style.render('лампочка', True, black)
    screen.blit(value, [1125, 100])
    # кнопки
    for button in massive_buttons:
        button.draw(screen)
