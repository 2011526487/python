'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
c=input('please input the first character')
if c=="M":
    print('Monday')
elif c=='W':
    print('Wednesday')
elif c=="F":
    print('Friday')
elif c=='T':
    c=input ( 'please input the second character' )
    if c=='u':
        print('Tuesday')
    elif c=='h':
        print('Thursday')
elif c=='S':
    c=input ( 'please input the second character' )
    if c=='a':
        print('Saturday')
    else:
        print('Sunday')
else:
    print('请输入正确的字符')
