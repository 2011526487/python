import turtle as t#画笔模块
import random
random.randint(0,256)
t.pensize(4)#尺寸
t.speed(0)#速度
t.penup()#提笔
t.tracer(True)#直接跳过过程，看结果
t.goto(0,0)#从中心点开始
t.pendown()#落笔
t.bgcolor('black')#背景颜色
(r,g,b)=(0,0,0)
for x in range(360):
    r=random.random()
    g=random.random()
    b=random.random()
    t.pencolor (r,g,b)  # 设画笔颜色
    t.forward(200)#设长度
    t.backward(200)#走回去走回来
    t.right(1)#走一个角度
t.done()#结束函数

