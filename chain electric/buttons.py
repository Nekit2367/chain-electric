import pygame as pg
# цвета
white=(255,255,255)
black=(0,0,0)
grey=(128,128,128)
button_DEFAULT_COLOR = (150, 150, 150)
button_HOVERED_COLOR = (120, 120, 120)
button_PRESSED_COLOR = (100, 100, 100)
pg.init()
screen=pg.display.set_mode((1300,800))
# создаем шрифты для текстов и пишем тексты
pg.font.init()
font_style = pg.font.SysFont("bahnschrift", 30) 
def write_text(text,x_position,y_position,screen,width,height,color):
    pg.draw.rect(screen,color,(x_position,y_position,width,height))
    value = font_style.render(text, True, black)
    screen.blit(value, [x_position+10, y_position+25])
class Button():
    def __init__(self,text,x,y,width,height):
        self.rect=self
        self.x=x
        self.y=y
        self.text=text
        self.width=width
        self.height=height
        self.color=button_DEFAULT_COLOR
    def button_down(self,event):
        if self.x<(pg.mouse.get_pos()[0])<self.x+self.width and self.y<(pg.mouse.get_pos()[1])<self.y+self.height: 
            if pg.event == pg.MOUSEBUTTONDOWN:
                self.color=button_PRESSED_COLOR
            else:
                self.color=button_HOVERED_COLOR
            return True
        else:
            self.color=button_DEFAULT_COLOR
            return False
    def draw(self,screen):
        write_text(self.text,self.x,self.y,screen,self.width,self.height,self.color)
    def ProcessEvents(self,event):
        if self.x<(pg.mouse.get_pos()[0])<self.x+self.width and self.y<(pg.mouse.get_pos()[1])<self.y+self.height: 
            self.color=button_PRESSED_COLOR        
        else:
            self.color=button_DEFAULT_COLOR