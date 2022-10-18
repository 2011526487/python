# i=0
# for baiwei in range(1,10):
#     for shiewei in range(0,10):
#         for gewei in range(0,10):
#             x= baiwei*100+shiewei*10+gewei
#             if (baiwei**3+shiewei**3+gewei**3==x):
#                 print(x,end = ' ')
#                 i+=1
# print('')
# print('1000以内有%d组水仙花数'%i)
# #___________________________________________
# b=0
# for i in range(100,1000):
#     baiwei=i//100
#     shiewei=(i//10)%10
#     gewei=i%10
#     x=baiwei*100+shiewei*10+gewei
#     if (baiwei ** 3 + shiewei ** 3 + gewei ** 3 == x) :
#         print ( x , end = ' ' )
#         b += 1
# print('')
# print('1000以内有%d组水仙花数'%i)
# #________________________________________
b=0
for i in range(100,1000):
    s=str(i)
    baiwei=int(s[0])
    shiewei=int(s[1])
    gewei=int(s[2])
    if (baiwei ** 3 + shiewei ** 3 + gewei ** 3 == i) :
        print ( i , end = ' ' )
        b += 1
print ( '' )
print ( '1000以内有%d组水仙花数' % i )



