import turtle
from turtle import  *
color('red','yellow')#第一个颜色是外勾边颜色，第二个是填充颜色,
goto(-100,0)
begin_fill()#先进行颜色填充
turtle.pensize(1)
for i in range(5):
    fd(200)#走200步
    rt(144)
end_fill()
done()



