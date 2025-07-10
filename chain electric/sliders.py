import pygame as pg
# цвета
white=(255,255,255)
black=(0,0,0)
pg.font.init()
font_style = pg.font.SysFont("bahnschrift", 30) 
class Slider():
    def buttondown(self):
        if self.x<(pg.mouse.get_pos()[0])<self.x+20 and self.y<(pg.mouse.get_pos()[1])<self.y+50: 
            return True
    def moving(self):
        x_new=(pg.mouse.get_pos()[0]-10)
        if self.x_0<=self.x<=self.x_0+160:
            if self.x_0<=x_new<=self.x_0+160:
                self.x=x_new
    def conclusion(self):
        return self.x
    def draw(self,screen):
        pg.draw.rect(screen,black,(self.x_0,self.y-5,180,60),2)
        pg.draw.line(screen,black,[self.x_0,self.y+25],[self.x_0+180,self.y+25],1)  
        pg.draw.rect(screen,black,(self.x,self.y,20,50))     
class Slider_resistor(Slider):
    def __init__(self):
        self.rect=self
        self.x_0=1100
        self.x=1100
        self.y=650
    def resistance(self):
        return ((self.conclusion()-1100)//1)
    def write(self,screen):
        value = font_style.render('R='+str(self.resistance())+' Ом', True, black)
        screen.blit(value, [1130, 707])

class Slider_voltage(Slider):
    def __init__(self):
        self.rect=self
        self.x=1100
        self.x_0=1100
        self.y=450
    def voltage(self):
        return ((self.conclusion()-1100)//4)
    def write(self,screen):
        value = font_style.render('V='+str(self.voltage())+'В', True, black)
        screen.blit(value, [1130, 507])

class Slider_position(Slider):
    def __init__(self):
        self.rect=self
        self.x=40
        self.x_0=40
        self.y=10
    def position(self):
        if self.x<120:
            return 'horisontal'
        else:
            return 'vertical'
    def write(self,screen):
        value = font_style.render(str(self.position()), True, black)
        screen.blit(value, [240, 20])
