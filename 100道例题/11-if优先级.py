x=int(input('请输入一个数做出判断'))
if (x %2==0 and x%3==0):
    print('该数字既能被二整除又能被三整除')
elif (x % 2 == 0 ) :
    print ( '该数字只能被二整除' )
elif (x % 3 == 0 ) :
    print ( '该数字只能被三整除' )
else:
    print('既不能被三整除也不能被二整除')