'''
题目：公鸡5元一只，母鸡三元一只 ，小鸡3只一元，用100元买100只鸡，其中公鸡母鸡，小鸡都必须有，
问公鸡，母鸡，小鸡要买多少只刚好凑足100元？
'''
(gj,mj,xj)=(5,3,1/3)
for x in range(100//5):
    for y in range(100//3):
        for z in range (100):
            if (x*gj+y*mj+z*xj==100 )and (x+y+z==100):
                print('公鸡{}只，母鸡{}只，小鸡{}只'.format(x,y,z))
