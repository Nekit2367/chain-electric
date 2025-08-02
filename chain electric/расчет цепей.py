import pygame as pg
import sys
from buttons import Button

from grid import Grid
from grid import Knot

from slider import Slider

from window import Window

from chain_parts import Resistor
from chain_parts import Voltage
from chain_parts import Diod
from chain_parts import Wire
from chain_parts import Lamp
from chain_parts import Condencator
from chain_parts import Inductor
from draw_chain import draw_fon

# цвета
white=(255,255,255)
black=(0,0,0)
# инициализация экрана
pg.init()
window=Window('Chain Electric',1550,800,60)
grid=Grid(1000,700,147) 
# создаем шрифты для текстов и пишем тексты
pg.font.init()
font_style = pg.font.SysFont("bahnschrift", 30) 
# создаем массив узлов
massive_knots=grid.GetMassive()       
# инициализируем ползунки
slider_resistor=Slider(220,60,0,100,0)
slider_voltage=Slider(220,60,0,100,0)
slider_condecator=Slider(220,60,0,100,0)
slider_inductance=Slider(220,60,0,100,0)
massive_sliders=[slider_resistor,slider_voltage,slider_condecator,slider_inductance]
# инициализируем кнопки
button_resistor=Button('add',1200,580,60,60)
button_voltage=Button('add',1200,460,60,60)
button_diod=Button('add',1300,160,60,60)
button_wire=Button('add',1300,240,60,60)
button_key=Button('add',1300,320,60,60)
button_lamp=Button('add',1300,80,60,60)
button_condencator=Button('add',1200,700,60,60)
button_inductor=Button('add',1200,820,60,60)
button_position=Button('change position',40,5,240,50)
button_delete=Button('delete',1100,10,95,60)
button_exit=Button('exit',1496,10,100,70)
massive_buttons=[button_resistor,button_voltage,button_diod,button_wire,button_lamp,button_position,button_delete,button_exit,button_condencator,button_inductor,button_key]
# класс массив
class Massive():
    def __init__(self):
        self.massive=[]
    def add_chain(self,chain,position):
        if chain==Resistor:
            part=chain(slider_resistor.GetValue(),position)
        elif chain==Voltage:
            part=chain(slider_voltage.GetValue(),position)
        else:
            part=chain(position)
        self.massive.append(part)
    def delete(self):
        if len(self.massive)>0:
            self.massive.pop()
    def draws(self,window):
        for i in range(len(self.massive)):
            self.massive[i].draw(window.GetScreen(),grid.targetDistance)
    def GetMassive(self):
        return self.massive
# класс рука
class Arm():
    def __init__(self):
        self.lead=False
        self.position='horisontal'
    # поиск ближайшего узла для того чтобы когда отпускаем деталь, деталь цеплялась сама к нужному узлу
    def found(self):
        x,y=pg.mouse.get_pos()
        mas_len=[]
        for i in range(len(massive_knots)):
            dist=(x-massive_knots[i].x)**2+(y-massive_knots[i].y)**2
            dist=dist**0.5
            mas_len.append(dist)
        z=mas_len.index(min(mas_len))
        return z
    # функция фиксации
    def fixing(self,massive):
        index=self.found()
        knot=massive_knots[index]
        massive[-1].new_x(knot.x)
        massive[-1].new_y(knot.y)   
        self.lead=False     
    # переноски элементов
    def moving_part(self,chain):
        chain.new_x(pg.mouse.get_pos()[0])
        chain.new_y(pg.mouse.get_pos()[1])  

    # меняем положение элементов (вертикаль/горизонталь)
    def change_position(self):
        if self.position=='horisontal':
            self.position='vertical'
        else:
            self.position='horisontal'
arm=Arm()
massive=Massive()
while True:
    for event in pg.event.get():
        window.ClearScreen(white)
        grid.Render(window.GetScreen())
        draw_fon(font_style,window.GetScreen(),massive_buttons,event)
        massive.draws(window)
        slider_resistor.Render(window.GetScreen(),1280,580,'Ом')
        slider_voltage.Render(window.GetScreen(),1280,460,'В')
        slider_condecator.Render(window.GetScreen(),1280,700,'мФ')
        slider_inductance.Render(window.GetScreen(),1280,820,'Гн')
        if event.type==pg.QUIT:
            sys.exit()
        elif event.type==pg.MOUSEBUTTONDOWN:
            if arm.lead:
                # фиксация элементов цепей
                arm.fixing(massive.massive)
            down=True
            # нажатие кнопок
            if button_resistor.button_down(event):
                arm.lead=True
                massive.add_chain(Resistor,arm.position)
            if button_voltage.button_down(event):
                arm.lead=True
                massive.add_chain(Voltage,arm.position)
            if button_diod.button_down(event):
                arm.lead=True
                massive.add_chain(Diod,arm.position)
            if button_wire.button_down(event):
                arm.lead=True
                massive.add_chain(Wire,arm.position)
            if button_lamp.button_down(event):
                arm.lead=True
                massive.add_chain(Lamp,arm.position)
            if button_condencator.button_down(event):
                arm.lead=True
                massive.add_chain(Condencator,arm.position)
            if button_inductor.button_down(event):
                arm.lead=True
                massive.add_chain(Inductor,arm.position)
            if button_position.button_down(event):
                arm.change_position()
            if button_delete.button_down(event):
                massive.delete()
            if button_exit.button_down(event):
                sys.exit()
    # пересчет значний
    slider_resistor.ProcessEvents(event)
    slider_voltage.ProcessEvents(event)
    slider_condecator.ProcessEvents(event)
    slider_inductance.ProcessEvents(event)
    #кнопки
    for i in range(len(massive_buttons)):
        massive_buttons[i].ProcessEvents(event)
    if arm.lead:
        arm.moving_part(massive.massive[-1])
    # # обновление экрана
    pg.display.update()
    pg.time.delay(15)


