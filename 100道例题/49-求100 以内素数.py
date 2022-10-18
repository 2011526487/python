a=int(input('范围初'))
b=int(input('范围末'))
def panduansushu (num):
    for i in range(2,num):
        if num%i==0:
            return  False
    return True
for x in range(a,b+1):
    if x>=2 and panduansushu(x):
        print(x,end = ' ')

