from turtle import *
bgcolor('black')
speed(0)
for i in range(200):
    if i%4==1:
        pencolor('red')
        fd(i*2)
        rt(90)
    elif i%4==2:
        pencolor('yellow')
        fd(i*2)
        rt(90)
    elif i%4==3:
        pencolor('white')
        fd(i*2)
        rt(90)
    if i%4==0:
        pencolor('blue')
        fd(i*2)
        rt(90)
done()