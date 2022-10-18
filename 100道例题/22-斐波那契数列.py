# #递归
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# n=int(input('n:'))
# print(fib(n))
#递推
n=int(input('n:'))
fib=[1,1]
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
print(fib[n-1])