
for i in range( 1 , 10 ) :
    for j in range( 1 , i + 1 ) :
        print( '%d*%d=%2d ' % (j , i , j * i) , end='' )
    print( '' )
# ————————————————————————————————————————————————————
for i in range(9,0,-1):
    for j in range(1,10-i):
        print('       ',end='')
    for j in range(1,i+1):
        print('%d*%d=%2d '%(i,j,i*j),end='')
    print('')
