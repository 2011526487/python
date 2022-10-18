'''
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
string=input('请输入一串字符串：')
letters=0#定义字母个数
spaces=0#定义空格个数
digits=0#定数字空格个数
others=0#定义其他个数
for i in string:
    if i.isalpha()==True:#判断字母的函数
        letters+=1
    elif i.isspace()==True:#判断空格的函数
        spaces+=1
    elif i.isdigit()==True:#判断数字的函数
        digits+=1
    else:
        others+=1
print('字母：%d,空格：%d,数字:%d,其他：%d'%(letters,spaces,digits,others))