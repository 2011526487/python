'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
# n=int(input('n:'))
# k=2
# while n!=1:
#     while n%k==0:
#         print(k,end = '')
#         n=n/k
#         if n!=1:
#             print('*',end = '')
#     k+=1
n=int(input('n:'))
for i  in range(2,n):
    if n!=0:
        if n%i==0:
            print(i,end = '')
            n=n/i
            if n!=1:
                print('*',end = '')
                for i in range(i,i+1):
                    if n % i == 0 :
                        print ( i , end = '' )
                        n = n / i
                        if n != 1 :
                            print ( '*' , end = '' )




