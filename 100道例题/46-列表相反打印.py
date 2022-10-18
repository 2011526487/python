'''
题目：按相反的顺序输出列表的值。
'''
list1=[]
n=int(input('请输入你要输几个数'))
for i in range(n):
    x=input('please input:')
    list1.append(x)
for i in list1[::-1]:
    print(i,end = '')
print('')
for i in range(n-1,-1,-1):
    print(list1[i],end = '')