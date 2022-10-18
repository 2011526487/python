c=1
k=3
for i in range(4):
    if k>0:
        for i in range(0,k):
            print(' ',end = '')
        k-=1
    if c<=4:
        for j in range(0,2*c-1):
            print('*',end = '')
        c+=1
    print()
a=1
b=3
for j in range(3):
    if a<=3:
        for i in range(0,a):
            print(' ',end = '')
        a+=1
    if b>0:
        for i in range(2*b-1,0,-1):
            print('*',end = '')
        b-=1
        print()
