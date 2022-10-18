'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
n=int(input('请输入想进行运算几行n:'))
a=int(input('请输入想要进行计算的最初数a:'))
t=a
sum=0
for i in range(n):
    sum += a
    print(a)
    a=a*10+t
    
print(sum)
