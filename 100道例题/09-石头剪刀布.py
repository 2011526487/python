print('1代表石头，2代表剪刀，3代表布')
print('三局两胜')
p,c=(0,0)
for i in range(3):
    import random
    player=int(input('请输入你想出的'))
    computer=random.randint(1,3)
    print('玩家%d,电脑%d'%(player,computer))
    if (player==1and computer==2)or(player==2and computer==3)or(player==3and computer==1):
        p+=1
    elif (player==computer):
        print('平局')
    else:
        c+=1
    if p==2:
        print('玩家胜利')
        break
    elif c==2:
        print('电脑胜利')
        break
print('')
if p>c:
    print('最终玩家胜利')
elif p==c:
    print('最终平局')
else:
    print('最终电脑胜利')