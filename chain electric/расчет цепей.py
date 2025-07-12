import pygame as pg
import sys
from buttons import Button

from slider import Slider

from window import Window

from chain_parts import Resistor
from chain_parts import Voltage
from chain_parts import Diod
from chain_parts import Wire
from chain_parts import Lamp
from draw_chain import draw_fon
# цвета
white=(255,255,255)
black=(0,0,0)
# инициализация экрана
pg.init()
window=Window('Chain Electric',1300,800,60)
# создаем шрифты для текстов и пишем тексты
pg.font.init()
font_style = pg.font.SysFont("bahnschrift", 30) 
# класс узел
class Knot():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw_point(self):
        pg.draw.circle(window.GetScreen(),black,(self.x,self.y),5)
# создаем массив узлов
massive_knots=[] #массив всех узлов
for i in range(5):
    mas=[]
    for j in range(4):
        knot=Knot(40+220*i,115+220*j)
        knot.draw_point()  
        mas.append(knot)
    massive_knots.append(mas)
# рисуем узлы
def draw_knotes():
    for i in range(5):
        for j in range(4):
            massive_knots[i][j].draw_point()          
# инициализируем ползунки
slider_resistor=Slider(180,60,0,100,0)
slider_voltage=Slider(180,60,0,100,0)
massive_sliders=[slider_resistor,slider_voltage]
# инициализируем кнопки
button_resistor=Button('add',1020,645,60,60)
button_voltage=Button('add',1020,445,60,60)
button_diod=Button('add',1110,185,60,60)
button_wire=Button('add',1130,285,60,60)
button_lamp=Button('add',1165,80,60,60)
button_position=Button('change position',40,5,240,60)
massive_buttons=[button_resistor,button_voltage,button_diod,button_wire,button_lamp,button_position]
# класс рука
class Arm():
    def __init__(self):
        self.lead=False
        self.massive=[]
        self.position='horisontal'
    # поиск ближайшего узла для того чтобы когда отпускаем деталь, деталь цеплялась сама к нужному узлу
    def found(self):
        x,y=pg.mouse.get_pos()
        mas_len=[]
        for i in range(5):
            for j in range(4):
                dist=(x-massive_knots[i][j].x)**2+(y-massive_knots[i][j].y)**2
                dist=dist**0.5
                mas_len.append(dist)
        z=mas_len.index(min(mas_len))
        return [z//4,z%4]
    # функция фиксации
    def fixing(self):
        index=self.found()
        knot=massive_knots[index[0]][index[1]]
        self.massive[-1].new_x(knot.x)
        self.massive[-1].new_y(knot.y)        
    # переноски элементов
    def moving_part(self):
        self.massive[-1].new_x(pg.mouse.get_pos()[0])
        self.massive[-1].new_y(pg.mouse.get_pos()[1])  
    # функция нажатие кнопки
    def button_down(self,chain):
        self.lead=True
        if chain==Resistor:
            part=chain(slider_resistor.GetValue(),self.position)
        elif chain==Voltage:
            part=chain(slider_voltage.GetValue(),self.position)
        else:
            part=chain(self.position)
        self.massive.append(part)
        return part
    # функция рисовки элементов
    def draws(self):
        for i in range(len(self.massive)):
            self.massive[i].draw(window.GetScreen())
    # меняем положение элементов (вертикаль/горизонталь)
    def change_position(self):
        if self.position=='horisontal':
            self.position='vertical'
        else:
            self.position='horisontal'
arm=Arm() 
while True:
    # рисовка фона
    draw_fon(font_style,window.GetScreen(),massive_buttons)
    draw_knotes()
    arm.draws()
    slider_resistor.Render(window.GetScreen(),1100,650)
    slider_voltage.Render(window.GetScreen(),1100,450)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        elif event.type==pg.MOUSEBUTTONDOWN:
            if arm.lead:
                # фиксация элементов цепей
                arm.fixing()
            arm.lead=False
            down=True
            # нажатие кнопок
            if button_resistor.button_down(event):
                resistor=arm.button_down(Resistor)
            if button_voltage.button_down(event):
                voltage=arm.button_down(Voltage)
            if button_diod.button_down(event):
                diod=arm.button_down(Diod)
            if button_wire.button_down(event):
                wire=arm.button_down(Wire)
            if button_lamp.button_down(event):
                lamp=arm.button_down(Lamp)
            if button_position.button_down(event):
                arm.change_position()
    # пересчет значний
    slider_resistor.ProcessEvents(event)
    slider_voltage.ProcessEvents(event)
    #кнопки
    button_resistor.ProcessEvents(event)
    button_voltage.ProcessEvents(event)
    button_wire.ProcessEvents(event)
    button_diod.ProcessEvents(event)
    button_lamp.ProcessEvents(event)
    button_position.ProcessEvents(event)
    if arm.lead:
        arm.moving_part()
    # обновление экрана
    pg.display.update()
    pg.time.delay(15)



