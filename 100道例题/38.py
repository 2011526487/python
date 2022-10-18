'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''
fenzi=[]
fenmu=[]
for i in range(0,20):
    if i==0:
        fenzi.append(2)
    elif i==1:
        fenzi.append(3)
    else:
        fenzi.append(fenzi[i-1]+fenzi[i-2])
for j in range(0,20):
    if j==0:
        fenmu.append(1)
    elif j==1:
        fenmu.append(2)
    else:
        fenmu.append(fenmu[j-2]+fenmu[j-1])
sum=0
t=0
for i in range(0,20):
    t=fenzi[i]/fenmu[i]
    sum+=t
print(sum)
