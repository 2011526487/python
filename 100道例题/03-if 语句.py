# number=int(input('请输入自己的成绩'))
# if number==100:
#     print('奖励一辆玩具车')
# if 80<=number<=99:
#     print('奖励一部新款电话手表')
# elif 60<=number<=79:
#     print('奖励一本书')
# else:
#     print('罚站一小时')
v0=25/3.6
g=9.8
y0=1
x=0.5
theta = int(input())  # 单位：角度
from math import tan,cos,pi
theta=theta/180*pi
#   请在此添加实现代码   #
# ********** Begin *********#
print(theta)
y=x*tan(theta)-1/(2*v0**2)*(g*x*x/cos(theta)*cos(theta))+y0

print("y值计算结果为：%.5f米"%y)


# ********** End **********#

