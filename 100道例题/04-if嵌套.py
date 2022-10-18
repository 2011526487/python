(a , b , c , d , e) = (0,0,0,0,0)
cishu = int ( input ( '请输入有多少组成绩：' ) )
for i in range ( cishu ) :
    number = int ( input ( '请输入成绩' ) )
    if 0 <= number <= 59 :
        print ( 'E' )
        e += 1
    if 60 <= number <= 69 :
        print ( 'D' )
        d += 1
    if 70 <= number <= 79 :
        print ( 'C' )
        c += 1
    if 80 <= number <= 89 :
        print ( 'B' )
        b += 1
    if 90 <= number <= 100 :
        print ( 'A' , end = '' )
        a += 1
        if number == 98 or number == 99 :
            print ( 'A' )
        elif number == 100 :
            print ( 'AA' )
        else :
            print ( '' )
print ( 'E有{}个，D有{}个，C有{}个，B有{}个，A有{}个'.format ( e , d , c , b , a ) )
