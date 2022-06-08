# https://www.acmicpc.net/problem/14442
from collections import deque
import sys
N, M, K = map(int, input().split())
graph = []
for i in range(N):
    tmp = list(map(int, input()))
    graph.append(tmp)

visited = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]
dq = deque([])
dq.append([0,0,0,1])

posx = [0,0,1,-1]
posy = [1,-1,0,0]

while dq:
    x,y,wall,result = dq.popleft()
    if x==M-1 and y==N-1:
        print(result)
        sys.exit()
    for i in range(4):
        tmpx = x+posx[i]
        tmpy = y+posy[i]
            
        if tmpx<0 or tmpx>=M or tmpy<0 or tmpy>=N:
            continue

        #벽을 부술 수 없는 경우, 벽이 아닌 경우
        if wall >= K and graph[tmpy][tmpx]==0:        
            if visited[tmpy][tmpx][wall] is False:
                visited[tmpy][tmpx][wall] = True
                dq.append([tmpx,tmpy,wall, result+1])
        #벽을 부술 수 있는 경우
        elif wall<K:
            walltmp = wall
            # 벽인 경우            
            if graph[tmpy][tmpx]==1:
                walltmp = wall+1
            if visited[tmpy][tmpx][walltmp] is False:
                visited[tmpy][tmpx][walltmp] = True
                dq.append([tmpx,tmpy,walltmp, result+1])
print(-1)