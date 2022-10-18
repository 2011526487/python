list=[]
n=int(input('请输入要输入的个数'))
for i in range(n):
    list.append(int(input('')))
list1=list[::2]#第一个空表从哪切，第二个空表切到那，第三个空表步长默认1
print(list1)