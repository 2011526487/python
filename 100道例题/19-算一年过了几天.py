year=int(input('请输入目前年份：'))
month=int(input('请输入目前月份：'))
day=int(input('请输入当前几号：'))
days=0
def is_runnian(year):
    if(year%4==0 and year%100!=00) or (year%400==0):
        return  True
    else:
        return  False
if is_runnian(year):
    months_days=[31,29,31,30,31,30,31,31,30,31,30,31]
else:
    months_days = [ 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31 ]
for i in range(0,month-1):
    days +=months_days[i]
days +=day-1
print('今年已经过去了%d'%days)