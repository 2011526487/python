'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
# t=0
# n=str(input('数字：'))
# for i in n:
#     t+=1
# print(t)
# for i in n:
#     t-=1
#     print(n[t],end = '')
#-----------------------
n=int(input('number:'))
a=n//10000
b=n//1000%10
c=n//100%10
d=n//10%10
e=n%10
if a!=0:
    print('五位数')
    print(e,d,c,b,a,end = '')
elif b!=0:
    print('四位数')
    print (  d , c , b , a , end = '' )
elif c!=0:
    print('三位数')
    print (  c , b , a , end = '' )
elif d!=0:
    print('二位数')
    print ( b , a , end = '' )
elif e!=0:
    print('一位数')
    print ( a)
