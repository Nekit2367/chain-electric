import pygame as pg
import sys
from sympy import symbols,Eq,solve
# 
from buttons import Button
# 
# from help_fucntion import Arm
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
green=(0,255,0)
blue=(0,0,255)
brown=(79, 70,0)
grey=(128,128,128)
# инициализация экрана
pg.init()
screen=pg.display.set_mode((1300,800))
pg.display.set_caption('расчет цепей')
# создаем шрифты для текстов и пишем тексты
pg.font.init()
font_style = pg.font.SysFont("bahnschrift", 30) \
# 
massive_numbers=[] #массив нереализован, должен записывать все пары пересечение(типо от узла 5 к узлу7 это 5,7)
for i in range(20):
    for j in range(20):
        if i!=j:
            massive_numbers.append([[i,j],[]])
# класс узел
class Knot():
    def __init__(self,x,y,number):
        self.circle=self
        self.x=x
        self.y=y
        self.voltage=0
        self.connection=[]
        self.number=number
    def connection_add(self,point):
        self.connection.append(point)
    def draw_point(self):
        pg.draw.circle(screen,black,(self.x,self.y),5)
# #################################вот это бредовык функции которые смотрят сколько вообще отдельных кусков схемы 
def neighboring_knot(knot_1,knot_2):
    knt_1=[0,0]
    knt_2=[0,0]
    knt_1[0]=(knot_1.x-40)/220
    knt_1[1]=(knot_1.y-115)/220
    knt_2[0]=(knot_2.x-40)/220
    knt_2[1]=(knot_2.y-115)/220
    if knot_2 in knot_1.connection:
        return True
    else:
        return False
def unnecessary_contacts(massive):
    mas=[]
    for knot in massive:
        if len(knot.connection)>1:
            mas.append(knot)
    return mas

def isolations(massive):
    massive=list(massive)
    massive_copy=massive.copy()
    massive_isolations=[]
    isolation=[]
    while len(massive_copy)!=0:
        el=massive_copy[0]
        massive_copy.remove(el)
        isolation.append(el)
        while True:
            p=0
            for knot in isolation.copy():
                kal=[]
                for i in range(len(massive_copy)):
                    new_el=massive_copy[i]
                    if neighboring_knot(knot,new_el):
                        isolation.append(new_el)
                        kal.append(new_el)
                        p=1
                for ii in range(len(kal)):
                    massive_copy.remove(kal[ii])
            if p==0:
                break
        massive_isolations.append(isolation)
        isolation=[]  
    return massive_isolations     
# ####################################################################



# создаем массив узлов
massive_knots=[] #массив всех узлов
massive_knots_work=set() #массив узлов, к которым хотя бы что то подсоединено
number=0
for i in range(5):
    mas=[]
    for j in range(4):
        knot=Knot(40+220*i,115+220*j,number)
        mas.append(knot)
        number+=1
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
# массивы элементов
massive_resistors=[]
massive_voltages=[]
massive_wires=[]
massive_diods=[]
massive_lamps=[]
# 
massive_variable=[] #нереализован, должен был быть для sympy
# класс рука
class Arm():
    def __init__(self):
        self.lead=False
        self.object=''
arm=Arm()
# функция смена падения потенциала
def new_drop_voltage(knot,index):
    if arm.object=='voltage':
        if slider_position.position()=='horisontal':
            knot.voltage=((massive_knots[index[0]+1][index[1]].voltage+slider_voltage.voltage()))
        else:
            knot.voltage=((massive_knots[index[0]][index[1]+1].voltage+slider_voltage.voltage()))  
    if arm.object=='wire':
        if slider_position.position()=='horisontal':
            knot.voltage=((massive_knots[index[0]+1][index[1]].voltage))
        else:
            knot.voltage=((massive_knots[index[0]][index[1]+1].voltage))   
    if arm.object=='resistor':
        var=symbols(chr(97+len(massive_variable)))
        if slider_position.position()=='horisontal':
            knot.voltage=((massive_knots[index[0]+1][index[1]].voltage+var))
        else:
            knot.voltage=((massive_knots[index[0]][index[1]+1].voltage+var)) 
        massive_resistors[-1].new_drop(var)
        massive_variable.append(var)  
# поиск ближайшего узла для того чтобы когда отпускаем деталь, деталь цеплялась сама к нужному узлу
def found(x,y):
    mas_len=[]
    for i in range(5):
        for j in range(4):
            dist=(x-massive_knots[i][j].x)**2+(y-massive_knots[i][j].y)**2
            dist=dist**0.5
            mas_len.append(dist)
    z=mas_len.index(min(mas_len))
    return [z//4,z%4]
def star(knot): # хотел сделать преобразование звезда треугольник
    knot_1=knot.connection[0]
    knot_2=knot.connection[1]
    knot_3=knot.connection[2]
    for i in range(len(massive_numbers)):
        if massive_numbers[i][0]==[knot,knot_1] or massive_numbers[i][0]==[knot_1,knot]:
            res=massive_numbers[i][1][0]
            R_1=res
            massive_numbers[i][1]=[]
        elif massive_numbers[i][0]==[knot,knot_2] or massive_numbers[i][0]==[knot_2,knot]:
            R_2=massive_numbers[i][1][0]
            massive_numbers[i][1]=[]
        elif massive_numbers[i][0]==[knot,knot_3] or massive_numbers[i][0]==[knot_3,knot]:
            R_3=massive_numbers[i][1][0]
            massive_numbers[i][1]=[]
    R_12=R_1+R_2+((R_1*R_2)/R_3)
    R_13=R_1+R_3+((R_1*R_3)/R_2)
    R_23=R_2+R_3+((R_2*R_3)/R_1)
    for i in range(len(massive_numbers)):
        if massive_numbers[i][0]==[knot_2,knot_1] or massive_numbers[i][0]==[knot_1,knot_2]:
            massive_numbers[i][1].append(R_12)
        elif massive_numbers[i][0]==[knot_3,knot_1] or massive_numbers[i][0]==[knot_1,knot_3]:
            massive_numbers[i][1].append(R_13)
        elif massive_numbers[i][0]==[knot_3,knot_2] or massive_numbers[i][0]==[knot_2,knot_3]:
            massive_numbers[i][1].append(R_23)
def parallel(): # а эта схема должна вроде считать параллельное сопротивление
    for i in range(len(massive_numbers)):
        k=massive_numbers[i]
        if len(k[1])>1:
            # k[1]=[
            for j in range(1,len(k[1])):
                k[1][0]+=k[1][j]
            k[1]=[k[1][0]]
            
# функция фиксации
def fixing(object,massive):
    index=found(object.conclusion_x(),object.conclusion_y())
    knot=massive_knots[index[0]][index[1]]
    massive_knots_work.add(knot)
    if slider_position.position()=='horisontal':
        k=massive_knots[index[0]+1][index[1]]
    else:
        k=massive_knots[index[0]][index[1]+1]
    massive_knots_work.add(k)
    knot.connection_add(k)
    k.connection_add(knot)
    if arm.object=='resistor':
        for i in range(len(massive_numbers)):
            if massive_numbers[i][0]==[knot.number,k.number] or massive_numbers[i][0]==[knot.number,k.number]:
                massive_numbers[i][1].append(slider_resistor.resistance())
    new_drop_voltage(knot,index)    
    massive[-1].new_x(knot.x)
    massive[-1].new_y(knot.y)
move_1=False
move_2=False
move_3=False
# переноски элементов
def moving_part(object):
    object.new_x(pg.mouse.get_pos()[0])
    object.new_y(pg.mouse.get_pos()[1])    
# функция нажатие кнопки
def button_down(object,chain,massive):
    arm.lead=True
    arm.object=object
    if chain==Resistor:
        part=chain(slider_resistor.resistance(),slider_position.position())
    elif chain==Voltage:
        part=chain(slider_voltage.voltage(),slider_position.position())
    else:
        part=chain(slider_position.position())
    massive.append(part)
    return part
# функция рисовки элементов
def draws(massive):
    for i in range(len(massive)):
        massive[i].draw(screen)
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
                if arm.object=="wire":
                    fixing(wire,massive_wires)
                if arm.object=="lamp":
                    fixing(lamp,massive_lamps)
                if arm.object=="resistor":
                    fixing(resistor,massive_resistors)
                if arm.object=="diod":
                    fixing(diod,massive_diods)
                if arm.object=="voltage":
                    fixing(voltage,massive_voltages)
            arm.lead=False
            down=True
            # нажатие кнопок
            if button_resistor.button_down():
                resistor=button_down('resistor',Resistor,massive_resistors)
            if button_voltage.button_down():
                voltage=button_down('voltage',Voltage,massive_voltages)
            if button_diod.button_down():
                diod=button_down('diod',Diod,massive_diods)
            if button_wire.button_down():
                wire=button_down('wire',Wire,massive_wires)
            if button_lamp.button_down():
                lamp=button_down('lamp',Lamp,massive_lamps)
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
        if arm.object=='wire':
            moving_part(wire)
        if arm.object=='resistor':
            moving_part(resistor)
        if arm.object=='voltage':
            moving_part(voltage)
        if arm.object=='diod':
            moving_part(diod)       
        if arm.object=='lamp':
            moving_part(lamp)
    # перебор массивов для рисовки элементов
    draws(massive_resistors)
    draws(massive_voltages)
    draws(massive_wires)
    draws(massive_diods)
    draws(massive_lamps)
    # обновление экрана
    pg.display.update()
    pg.time.delay(15)
