'''
题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。请问第五个人多大？
'''
#递推
age=[10]
n=int(input('请输入想查询第几个人年龄'))
for i in range(1,n):
    age.append(age[i-1]+2)
print(age[n-1])
#递归
age=[10]
n=int(input('请输入想查询第几个人年龄'))
def age(n):
    if n==1:
        return 10
    return age(n-1)+2
print(age(n))