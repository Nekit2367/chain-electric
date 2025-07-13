import pygame as pg
# цвета
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
grey=(128,128,128)
class Element():
    def __init__(self,position):
        self.x=pg.mouse.get_pos()[0]
        self.y=pg.mouse.get_pos()[1]
        self.voltage_drop=0
        self.position=position
        self
    def new_x(self,x_new):
        self.x=x_new
    def new_y(self,y_new):
        self.y=y_new
    def conclusion_x(self):
        return self.x
    def conclusion_y(self):
        return self.y
    def conclus(self):
        return self.nominale 
class Resistor(Element):
    def __init__(self,nominal,position):
        Element.__init__(self,position)
        self.nominale=nominal
    def draw(self,screen):        
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+100,self.y],2)
            pg.draw.rect(screen,black,(self.x+18,self.y-8,64,14))
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+100],2)
            pg.draw.rect(screen,black,(self.x-8,self.y+18,14,64))
class Voltage(Element):
    def __init__(self,nominal,position):
        Element.__init__(self,position)
        self.nominale=nominal
    def draw(self,screen):        
        if self.position=='horisontal':
            pg.draw.line(screen,black,(self.x,self.y),(self.x+41,self.y),2)
            pg.draw.line(screen,black,(self.x+59,self.y),(self.x+100,self.y),2)
            pg.draw.line(screen,black,(self.x+41,self.y-18),(self.x+41,self.y+18),2)
            pg.draw.line(screen,black,(self.x+59,self.y-9),(self.x+59,self.y+9),2)
        else:
            pg.draw.line(screen,black,(self.x,self.y),(self.x,self.y+41),2)
            pg.draw.line(screen,black,(self.x,self.y+59),(self.x,self.y+100),2)
            pg.draw.line(screen,black,(self.x-18,self.y+41),(self.x+18,self.y+41),2)
            pg.draw.line(screen,black,(self.x-9,self.y+59),(self.x+9,self.y+59),2)
class Diod(Element):
    def __init__(self,position):
        Element.__init__(self,position)
    def draw(self,screen):
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+100,self.y],2)
            pg.draw.lines(screen,black,True,[[self.x+59,self.y-18],[self.x+59,self.y+18],[self.x+32,self.y]])
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+100],2)
            pg.draw.lines(screen,black,True,[[self.x-18,self.y+59],[self.x+18,self.y+59],[self.x,self.y+32]])
class Wire(Element):
    def __init__(self,position):
        Element.__init__(self,position)
    def draw(self,screen):
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+100,self.y],2)
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+100],2)
class Lamp(Element):
    def __init__(self,position):
        Element.__init__(self,position)
        self.nominale=10  
    def draw(self,screen):
        if self.position=='horisontal':
            pg.draw.circle(screen,black,(self.x+50,self.y),18,3)
            pg.draw.line(screen,black,[self.x,self.y],[self.x+32,self.y],2)
            pg.draw.line(screen,black,[self.x+68,self.y],[self.x+100,self.y],2)
            pg.draw.line(screen,black,[self.x+40,self.y-10],[self.x+60,self.y+10],2)
            pg.draw.line(screen,black,[self.x+60,self.y-10],[self.x+40,self.y+10],2)
        else:
            pg.draw.circle(screen,black,(self.x,self.y+50),18,3)
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+32],2)
            pg.draw.line(screen,black,[self.x,self.y+68],[self.x,self.y+100],2)
            pg.draw.line(screen,black,[self.x-10,self.y+40],[self.x+10,self.y+60],2)
            pg.draw.line(screen,black,[self.x+10,self.y+40],[self.x-10,self.y+60],2)

