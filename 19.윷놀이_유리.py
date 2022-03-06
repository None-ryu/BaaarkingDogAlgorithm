# https://www.acmicpc.net/problem/2490

for i in range(3):
    cnt = 0
    num = list(map(int, input().split()))
    
    for n in num:
        if n == 0:
            cnt+=1
    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    elif cnt == 0:
        print('E')