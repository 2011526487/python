# from turtle import *#全部导入
# speed(100000)#速度最快
# color('red')
# bgcolor('black')
# pensize(3)
# for x in range(20):
#     circle(100)#(radius半径，extent=None弧度，steps=None边数)
#     right(18)#向右旋转
# done()
#___________________________________
# from turtle import * #全部导入
# speed(0)#速度最快
# import random#随即模块
# random.randint(0,256)
# bgcolor('black')
# pensize(3)
# for x in range(20):
#     r=random.random()
#     g=random.random()
#     b=random.random()
#     color(r,g,b)
#     circle(100)#(radius半径，extent=None弧度，steps=None边数)
#     right(18)#向右旋转
# done()
#_________________________________
#彩虹
# from turtle import *
# speed(0)
# import random#随即模块
# random.randint(0,256)
# goto(0,0)
# pensize(7)
# y=0
# bgcolor('white')
# tracer(False)
# for x in range(9):
#     setheading ( 90 )  # 规定了起始方向为水平
#     goto(0,y)
#     pendown()
#     circle(100,360)
#     r = random.random ()
#     g = random.random ()
#     b = random.random ()
#     color ( r , g , b )
#     penup()
#     y-=7
# done()
#______________________________________
#管道
# from turtle import  *
# speed(0)
# pensize(3)
# bgcolor('white')
# tracer(False)
# penup()
# x=50#定义s的起始点
# for i in range(40):#意思是长为30的管道
#     setheading(90)
#     goto(x,0)
#     pendown()#落笔
#     color('black')
#     circle(120,180)
#     color('gray')
#     circle(120,180)
#     penup()#抬笔
#     x+=2
# done()

import turtle as t
t.speed(10)
t.color('red')
t.bgcolor('black')
t.pensize(3)
for x in range(20):
    t.circle(100)
    t.right(18)
t.done()