import pygame as pg
import math
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
        self.thickness=2
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
    def draw(self,screen,distance):       
        self.width=round(distance/12) 
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+distance,self.y],self.thickness)
            pg.draw.rect(screen,black,(self.x+round(distance/5),self.y-self.width,round(3*distance/5),2*self.width))
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+distance],self.thickness)
            pg.draw.rect(screen,black,(self.x-self.width,self.y+round(distance/5),2*self.width,round(3*distance/5)))
class Voltage(Element):
    def __init__(self,nominal,position):
        Element.__init__(self,position)
        self.nominale=nominal
    def draw(self,screen,distance):        
        if self.position=='horisontal':
            pg.draw.line(screen,black,(self.x,self.y),(self.x+round(2*distance/5),self.y),self.thickness)
            pg.draw.line(screen,black,(self.x+round(3*distance/5),self.y),(self.x+round(distance),self.y),self.thickness)
            pg.draw.line(screen,black,(self.x+round(2*distance/5),self.y-round(distance/5)),(self.x+round(2*distance/5),self.y+round(distance/5)),self.thickness)
            pg.draw.line(screen,black,(self.x+round(3*distance/5),self.y-round(distance/10)),(self.x+round(3*distance/5),self.y+round(distance/10)),self.thickness)
        else:
            pg.draw.line(screen,black,(self.x,self.y),(self.x,self.y+round(2*distance/5)),self.thickness)
            pg.draw.line(screen,black,(self.x,self.y+round(3*distance/5)),(self.x,self.y+distance),self.thickness)
            pg.draw.line(screen,black,(self.x-round(distance/5),self.y+round(2*distance/5)),(self.x+round(distance/5),self.y+round(2*distance/5)),self.thickness)
            pg.draw.line(screen,black,(self.x-round(distance/10),self.y+round(3*distance/5)),(self.x+round(distance/10),self.y+round(3*distance/5)),self.thickness)
class Diod(Element):
    def __init__(self,position):
        Element.__init__(self,position)
    def draw(self,screen,distance):
        self.side=round(distance/4)
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+distance,self.y],self.thickness)
            pg.draw.lines(screen,black,True,[[self.x+distance/2-round(((3**0.5)/4)*self.side),self.y],[self.x+distance/2+round(((3**0.5)/4)*self.side),self.y+round(self.side/2)],[self.x+distance/2+round(((3**0.5)/4)*self.side),self.y-round(self.side/2)]],self.thickness)
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+distance],2)
            pg.draw.lines(screen,black,True,[[self.x-round(self.side/2),self.y+distance/2-round(((3**0.5)/4)*self.side)],[self.x+round(self.side/2),self.y+distance/2-round(((3**0.5)/4)*self.side)],[self.x,self.y+distance/2+round(((3**0.5)/4)*self.side)]],self.thickness)
class Wire(Element):
    def __init__(self,position):
        Element.__init__(self,position)
        self.thickness=2
    def draw(self,screen,distance):
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+distance,self.y],self.thickness)
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+distance],self.thickness)
class Lamp(Element):
    def __init__(self,position):
        Element.__init__(self,position)
        self.nominale=10 
    def draw(self,screen,distance):
        self.R=round(distance/5)
        if self.position=='horisontal':
            pg.draw.circle(screen,black,(self.x+distance/2,self.y),self.R,self.thickness)
            pg.draw.line(screen,black,[self.x,self.y],[self.x+distance/2-self.R,self.y],self.thickness)
            pg.draw.line(screen,black,[self.x+round(distance/2)+self.R,self.y],[self.x+distance,self.y],self.thickness)
            pg.draw.line(screen,black,[self.x+round(distance/2-self.R/(2**0.5)),self.y-round(self.R/(2**0.5))],[self.x+distance/2+round(self.R/(2**0.5)),self.y+round(self.R/(2**0.5))],self.thickness)
            pg.draw.line(screen,black,[self.x+round(distance/2+self.R/(2**0.5)),self.y-round(self.R/(2**0.5))],[self.x+round(distance/2-self.R/(2**0.5)),self.y+round(self.R/(2**0.5))],self.thickness)
        else:
            pg.draw.circle(screen,black,(self.x,self.y+distance/2),self.R,self.thickness)
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+distance/2-self.R],self.thickness)
            pg.draw.line(screen,black,[self.x,self.y+round(distance/2)+self.R],[self.x,self.y+distance],self.thickness)
            pg.draw.line(screen,black,[self.x-round(self.R/(2**0.5)),self.y+round(distance/2-self.R/(2**0.5))],[self.x+round(self.R/(2**0.5)),self.y+round(distance/2+self.R/(2**0.5))],self.thickness)
            pg.draw.line(screen,black,[self.x+round(self.R/(2**0.5)),self.y+round(distance/2-self.R/(2**0.5))],[self.x-round(self.R/(2**0.5)),self.y+round(distance/2+self.R/(2**0.5))],self.thickness)

class Condencator(Element):
    def __init__(self,position):
        Element.__init__(self,position)
        self.nominale=10 
    def draw(self,screen,distance):
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+round(2*distance/5),self.y],self.thickness)
            pg.draw.line(screen,black,[self.x+round(3*distance/5),self.y],[self.x+distance,self.y],self.thickness)
            pg.draw.line(screen,black,[self.x+round(2*distance/5),self.y-round(distance/4)],[self.x+round(2*distance/5),self.y+round(distance/4)],self.thickness)
            pg.draw.line(screen,black,[self.x+round(3*distance/5),self.y-round(distance/4)],[self.x+round(3*distance/5),self.y+round(distance/4)],self.thickness)
        else:
            pg.draw.line(screen,black,[self.x,self.y],[self.x,self.y+round(2*distance/5)],self.thickness)
            pg.draw.line(screen,black,[self.x,self.y+round(3*distance/5)],[self.x,self.y+distance],self.thickness)
            pg.draw.line(screen,black,[self.x-round(distance/4),self.y+round(2*distance/5)],[self.x+round(distance/4),self.y+round(2*distance/5)],self.thickness)
            pg.draw.line(screen,black,[self.x-round(distance/4),self.y+round(3*distance/5)],[self.x+round(distance/4),self.y+round(3*distance/5)],self.thickness)
class Inductor(Element):
    def __init__(self,position):
        Element.__init__(self,position)
        self.nominale=10 
    def draw(self,screen,distance):
        self.side=round(distance/5)
        if self.position=='horisontal':
            pg.draw.line(screen,black,[self.x,self.y],[self.x+self.side,self.y],self.thickness)
            pg.draw.line(screen,black,[self.x+distance-self.side,self.y],[self.x+distance,self.y],self.thickness)
            pg.draw.arc(screen,black,[self.x+self.side,self.y-13,self.side+1,self.side+1],0,math.pi,width=self.thickness)
            pg.draw.arc(screen,black,[self.x+2*self.side,self.y-13,self.side+1,self.side+1],0,math.pi,width=self.thickness)
            pg.draw.arc(screen,black,[self.x+3*self.side,self.y-13,self.side+1,self.side+1],0,math.pi,width=self.thickness)
        else:
            pass
