'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
(a>b) ? a:b
'''
grade=int(input('请输入你的成绩：'))
if grade>=90:
    print('%d属于A'%grade)
elif grade>=60:
    print('%d属于B'%grade)
else:
    print('%d属于C'%grade)
