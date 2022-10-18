'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
'''
def output(string,lenth):
    if lenth==0:
        return
    print(string[lenth-1],end = '')
    output(string,lenth-1)
output('abcde',len('abcde'))