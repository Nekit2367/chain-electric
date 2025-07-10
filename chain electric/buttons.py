import pygame as pg
# цвета
white=(255,255,255)
black=(0,0,0)
grey=(128,128,128)
pg.init()
screen=pg.display.set_mode((1300,800))
# создаем шрифты для текстов и пишем тексты
pg.font.init()
font_style = pg.font.SysFont("bahnschrift", 30) 
def write_add(x,y,screen):
    pg.draw.rect(screen,grey,(x,y,60,60))
    value = font_style.render('add', True, black)
    screen.blit(value, [x+10, y+25])
    # 1020 645
class Button():
    def __init__(self,x,y):
        self.rect=self
        self.x=x
        self.y=y
    def button_down(self):
        if self.x<(pg.mouse.get_pos()[0])<self.x+60 and self.y<(pg.mouse.get_pos()[1])<self.y+60: 
            return True
        else:
            return False
    def draw(self,screen):
        write_add(self.x,self.y,screen)
