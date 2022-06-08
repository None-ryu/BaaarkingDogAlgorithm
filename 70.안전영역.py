# https://www.acmicpc.net/problem/6593
from collections import deque
import sys
M, N, H = map(int, input().split())

graph = []
dq = deque([])
for h in range(H):
    graph.append([])
    for n in range(N):   
        tmplist = list(map(int, sys.stdin.readline().split()))       # sys.stdin.readline().split() 없으면 시간초과남
        graph[h].append(tmplist)        
        for num in range(len(tmplist)):            
            if tmplist[num] == 1:
                dq.append([num,n,h, 0])

# for h in range(H):
#     for n in range(N): 
#         for m in range(M): 
#             print(graph[h][n][m], sep=" ")

xpos = [0,0,1,-1, 0, 0]
ypos = [1,-1,0,0, 0, 0]
hpos = [0,0,0,0, 1, -1]
lastcnt = 0
while dq:
    x, y, h, cnt = dq.popleft()
    graph[h][y][x] = 1

    for i in range(6):
        tmpx = x + xpos[i]
        tmpy = y + ypos[i]
        tmph = h + hpos[i]        
        if 0<=tmpx<M and 0<=tmpy<N and 0<=tmph<H and graph[tmph][tmpy][tmpx]==0:
            graph[tmph][tmpy][tmpx] = 1
            dq.append([tmpx, tmpy, tmph, cnt+1])
            lastcnt = cnt+1

for h in range(H):
    for n in range(N): 
        for m in range(M): 
            if graph[h][n][m] == 0:                
                print(-1)
                sys.exit()                
   
print(lastcnt)
