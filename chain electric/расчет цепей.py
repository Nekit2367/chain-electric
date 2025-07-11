import pygame as pg
import sys
from buttons import Button
# 
from sliders import Slider_resistor
from sliders import Slider_voltage
from sliders import Slider_position
# 
from chain_parts import Resistor
from chain_parts import Voltage
from chain_parts import Diod
from chain_parts import Wire
from chain_parts import Lamp
# 
from draw_chain import draw_fon
# цвета
white=(255,255,255)
black=(0,0,0)
# инициализация экрана
pg.init()
screen=pg.display.set_mode((1300,800))
pg.display.set_caption('расчет цепей')
# создаем шрифты для текстов и пишем тексты
pg.font.init()
font_style = pg.font.SysFont("bahnschrift", 30) 
# класс узел
class Knot():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw_point(self):
        pg.draw.circle(screen,black,(self.x,self.y),5)
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
slider_resistor=Slider_resistor()
slider_voltage=Slider_voltage()
slider_position=Slider_position()
massive_sliders=[slider_resistor,slider_voltage,slider_position]
# фиксатор нажатия
down=False
# инициализируем кнопки
button_resistor=Button(1020,645)
button_voltage=Button(1020,445)
button_diod=Button(1110,185)
button_wire=Button(1130,285)
button_lamp=Button(1165,80)
massive_buttons=[button_resistor,button_voltage,button_diod,button_wire,button_lamp]
# класс рука
class Arm():
    def __init__(self):
        self.lead=False
        self.massive=[]
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
            part=chain(slider_resistor.resistance(),slider_position.position())
        elif chain==Voltage:
            part=chain(slider_voltage.voltage(),slider_position.position())
        else:
            part=chain(slider_position.position())
        self.massive.append(part)
        return part
    # функция рисовки элементов
    def draws(self):
        for i in range(len(self.massive)):
            self.massive[i].draw(screen)
move_1=False
move_2=False
move_3=False 
arm=Arm() 
while True:
    # рисовка фона
    draw_fon(font_style,screen,massive_buttons,massive_sliders)
    draw_knotes()
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
            if button_resistor.button_down():
                resistor=arm.button_down(Resistor)
            if button_voltage.button_down():
                voltage=arm.button_down(Voltage)
            if button_diod.button_down():
                diod=arm.button_down(Diod)
            if button_wire.button_down():
                wire=arm.button_down(Wire)
            if button_lamp.button_down():
                lamp=arm.button_down(Lamp)
        elif event.type==pg.MOUSEBUTTONUP:
            # сброс
            down=False
            move_1=False
            move_2=False
            move_3=False
    # ползунки
    if down:
        if move_1:
            slider_resistor.moving()
        else:
            move_1=slider_resistor.buttondown()
        if move_2:
            slider_voltage.moving()
        else:
            move_2=slider_voltage.buttondown()
        if move_3:
            slider_position.moving()
        else:
            move_3=slider_position.buttondown()
    # добавление новых элементов
    if arm.lead:
        arm.moving_part()
    # перебор массивов для рисовки элементов
    arm.draws()
    # обновление экрана
    pg.display.update()
    pg.time.delay(15)
