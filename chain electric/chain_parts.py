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
            pg.draw.line(screen,black,[self.x,self.y],[self.x+220,self.y],2)
            pg.draw.rect(screen,black,(self.x+40,self.y-15,140,30))
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+220],2)
            pg.draw.rect(screen,black,(self.x-15,self.y+40,30,140))
class Voltage(Element):
    def __init__(self,nominal,position):
        Element.__init__(self,position)
        self.nominale=nominal
    def draw(self,screen):        
        if self.position=='horisontal':
            pg.draw.line(screen,black,(self.x,self.y),(self.x+90,self.y),2)
            pg.draw.line(screen,black,(self.x+130,self.y),(self.x+220,self.y),2)
            pg.draw.line(screen,black,(self.x+90,self.y-40),(self.x+90,self.y+40),2)
            pg.draw.line(screen,black,(self.x+130,self.y-20),(self.x+130,self.y+20),2)
        else:
            pg.draw.line(screen,black,(self.x,self.y),(self.x,self.y+90),2)
            pg.draw.line(screen,black,(self.x,self.y+130),(self.x,self.y+220),2)
            pg.draw.line(screen,black,(self.x-40,self.y+90),(self.x+40,self.y+90),2)
            pg.draw.line(screen,black,(self.x-20,self.y+130),(self.x+20,self.y+130),2)
class Diod(Element):
    def __init__(self,position):
        Element.__init__(self,position)
    def draw(self,screen):
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+220,self.y],2)
            pg.draw.lines(screen,black,True,[[self.x+130,self.y-40],[self.x+130,self.y+40],[self.x+70,self.y]])
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+220],2)
            pg.draw.lines(screen,black,True,[[self.x-40,self.y+130],[self.x+40,self.y+130],[self.x,self.y+70]])
class Wire(Element):
    def __init__(self,position):
        Element.__init__(self,position)
    def draw(self,screen):
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+220,self.y],2)
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+220],2)
class Lamp(Element):
    def __init__(self,position):
        Element.__init__(self,position)
        self.nominale=10  
    def draw(self,screen):
        if self.position=='horisontal':
            pg.draw.circle(screen,black,(self.x+110,self.y),40,5)
            pg.draw.line(screen,black,[self.x,self.y],[self.x+70,self.y],2)
            pg.draw.line(screen,black,[self.x+150,self.y],[self.x+220,self.y],2)
            pg.draw.line(screen,black,[self.x+87,self.y-23],[self.x+133,self.y+23],2)
            pg.draw.line(screen,black,[self.x+133,self.y-23],[self.x+87,self.y+23],2)
        else:
            pg.draw.circle(screen,black,(self.x,self.y+110),40,5)
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+70],2)
            pg.draw.line(screen,black,[self.x,self.y+150],[self.x,self.y+220],2)
            pg.draw.line(screen,black,[self.x-23,self.y+87],[self.x+23,self.y+133],2)
            pg.draw.line(screen,black,[self.x+23,self.y+87],[self.x-23,self.y+133],2)

