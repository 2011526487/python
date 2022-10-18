'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
1:a
2:a
3:a a1
4:a a1 a2
5: a a1 a2 a3 a11
6:a a1 a2 a3 a4 a11 a12 a21
7:a a1 a2 a3 a4 a11 a12 a21
'''
n=int(input('请输入你想看几个月的兔子数量'))
rabbits=[1,1]
for i in range(2,n):
    rabbits.append(rabbits[i-1]+rabbits[i-2])
print('第%d个月的兔子数量有%d只'%(n,rabbits[n-1]))