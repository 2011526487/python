'''
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''
# for i in range(2,1001):
#     yinzi=[]
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             yinzi.append(j)
#             sum+=j
#     if sum==i:
#         print(i,end = '=')
#         yinzi.reverse()
#         for k in yinzi:
#             print(k,end = '')
#             if k!=1:
#                 print('+',end = '')
#         print('',end = ' ')
# #-------------------------------------
# for i in range(2,1001):
#     yinzi=[]
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             yinzi.append(j)
#             sum+=j
#     if sum==i:
#         print(i)
#         for j in yinzi:
#             print(j,end = ' ')
#         print()
#------------------------n=0
for i in range(2,1001):
    yinzi=[]
    sum=0
    n=0
    for j in range(1,i):
        if i%j==0:
            yinzi.append(j)
            n=n+1
            sum+=j
    if sum==i:
        print(i,end = '=')
        for j in yinzi:
            p=yinzi.index(j)
            if p!=n-1:
                print(j,end = '+')
            else:
                print(j,end = '')
        print()




