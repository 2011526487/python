"""
用1、3、5、8这几个数字，能组成的互不相同且无重复数字的三位数各是多少？总共有多少个？
"""
list1=['1','3','5','8']
n=0
for x in list1:
    for y in list1:
        for z in list1:
            if (x!=y and x!=z and y!=z):
                print(x+y+z,end = ' ')
                n+=1
print('')
print('一共有%d组'%n)
