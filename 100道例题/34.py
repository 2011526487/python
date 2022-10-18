'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
total =100
tan=50
for i in range(9):
    total=total+tan*2
    tan=tan/2
print(total)
print(tan)
