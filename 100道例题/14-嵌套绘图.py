from turtle import *
bgcolor('black')
pencolor('pink')
def HT(side,sides):
    for i in range(sides):
        fd (side)
        rt(360/sides)
for x in range(10):
    HT(100,5)#(尺度，边数)
    rt(360/10)#(最后所有图形围成的度数，有几个这种形状构成)
done()