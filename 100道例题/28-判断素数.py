'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''
# 1
# def panduansushu(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#
#     return True
# t=0
# s=0
# for i in range(101,201):
#     if panduansushu(i):
#         t+=1
#         print(i,end = ' ')
#         s+=1
#     if s==10:
#         print()
#         s=0
# print()
# print('有%d组'%t)
#2
import math
def panduansushu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False

    return True
t=0
s=0
for i in range(101,201):
    if panduansushu(i):
        t+=1
        print(i,end = ' ')
        s+=1
    if s==10:
        print()
        s=0
print()
print('有%d组'%t)

