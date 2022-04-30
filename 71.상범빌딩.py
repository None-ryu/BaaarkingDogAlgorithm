# https://www.acmicpc.net/problem/6593
from collections import deque
import sys
while True:
    # H 높이 / N Y축 / M X축
    H, N, M = map(int, input().split())
    ex, ey, eh = -1, -1, -1

    if H==0 and N==0 and M==0:
        break
    graph = []
    dq = deque([])
    for h in range(H):
        graph.append([])
        for n in range(N):   
            tmplist = list(sys.stdin.readline().strip())      # sys.stdin.readline().split() 없으면 시간초과남
            graph[h].append(tmplist)        
            for num in range(len(tmplist)):            
                if tmplist[num] == 'S':
                    dq.append([num,n,h, 0])
                elif tmplist[num] == 'E':
                    ex = num
                    ey = n
                    eh = h
        input()        
    # for h in range(H):
    #     for n in range(N): 
    #         for m in range(M): 
    #             print(graph[h][n][m], sep=" ")

    xpos = [0,0,1,-1, 0, 0]
    ypos = [1,-1,0,0, 0, 0]
    hpos = [0,0,0,0, 1, -1] 
    flag = False   
    while dq:
        x, y, h, cnt = dq.popleft()
        if graph[h][y][x] == 'E':
            print("Escaped in",cnt,"minute(s).")
            flag = True
            break
        graph[h][y][x] = 'V'

        for i in range(6):
            tmpx = x + xpos[i]
            tmpy = y + ypos[i]
            tmph = h + hpos[i]        
            if 0<=tmpx<M and 0<=tmpy<N and 0<=tmph<H and (graph[tmph][tmpy][tmpx]=='.' or graph[tmph][tmpy][tmpx]=='E'):
                if graph[tmph][tmpy][tmpx]=='.':
                    graph[tmph][tmpy][tmpx] = 'V'
                dq.append([tmpx, tmpy, tmph, cnt+1])                
    if flag is False:
        print("Trapped!")