n=0
for baiwei in range (1,5):
    for shiwei in range (1,5):
        for gewei  in range (1,5):
            if (baiwei!=shiwei and baiwei != gewei and shiwei != gewei):
                print("%d%d%d"%(baiwei,shiwei,gewei))
                n+=1
print('有%d组'%n)
