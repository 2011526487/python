# #题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# #（1）排序算法（用sort）
# l=[]
# print('请依次输入想比较大小的三个数：')
# for i in range(3):
#     x=int(input('第%d个'%(i+1)))
#     l.append(x)
# l.sort()
# print('从小到大排',end = '')
# print(l)
# l1=sorted(l,reverse = False)#从大到小排
# print('从小到大排',end = '')
# print(l1)
# l2=sorted(l)
# print('从小到大排',end = '')
# print(l2)
#
#
# l.reverse()
# print('从大到小排',end = '')
# print(l)
# l3=sorted(l,reverse = True)#从大到小排
# print('从大到小排',end = '')
# print(l3)
#第二种逐个比较
print('请依次输入想比较大小的三个数：')
x=int(input('x:'))
y=int(input('y:'))
z=int(input('z:'))
t=0
if x<y:
    if x<z:
        t=x
        if y<z:
            x=y
            y=z
        else:
            x=z
            y=y
    else:
        t=z
elif x>y:
    if x>z:
        if y<z:
            t=y
            y=x
            x=z
        else:
            t=z
            z=x
            x=y
            y=z
    else:
        t=y
        x=x
        y=z
else:
    if x<z:
        t=y
        x=x
        y=z
print(t,x,y)


