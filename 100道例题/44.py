'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
n=str(input('number:'))
flag=True
for i in range(0,len(n)//2):
    if n[i]!=n[len(n)-i-1]:
        flag=False
        break
if(flag):
    print('它是一个回文数')
else:
    print('它不是')


