# '''
# 题目：对10个数进行排序。
# '''
# N=10
# print('请输入10个数字')
# l=[]
# for i in range(N):
#     n=int(input('请输入第%d个数'%(i+1)))
#     l.append(n)
# for i in range(N):
#     min=i
#     for j in range(i+1,N):
#         if l[j]<l[min]:
#             min =j
#     l[i],l[min]=l[min],l[i]
# print(l)
str="asbfgh"
a=str[-1:-3]
print(a)
print("_ "*10)
s="asdkjgik"
print(s.find("dk",0,5))#0,5从序号0开始到5结束5不取

print(s.count("as"))
strs="one two three"
b=strs.strip()
print(b)#分割
print(",".join(strs))#添加
print(strs.replace(" ","-"))
strs1='   PWEKBPTKBP    '
print(strs1.strip(" "))
# print(strs1.lower())#转换小写
print(strs1.upper())#转换大写


