n=0
for i in range(1,101):
    if i%7!=0:
        print('%2d'%i,end = ' ')
        n+=1
    if n==10:
        print()
        n=0
