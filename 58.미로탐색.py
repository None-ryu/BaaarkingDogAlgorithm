# https://www.acmicpc.net/problem/2178
from collections import deque
N, M = map(int, input().split())
graph = []
for i in range(N):
    tlist = list(map(int, input()))
    graph.append(tlist)

visited = [ [False]*M for _ in range(N)]

def bfs(x, y):
    dx = [0, 0 , 1, -1]
    dy = [1, -1, 0, 0]    
    dq = deque([])
    dq.append([x, y, 1])
    visited[y][x] = True
    while dq:
        xx, yy, cnt = dq.popleft()                
        if xx == M-1 and yy == N-1:            
            print(cnt)
            return

        for i in range(4):
            tmpx = xx+dx[i]
            tmpy = yy+dy[i]

            if 0<=tmpx<M and 0<=tmpy<N and visited[tmpy][tmpx] is False and graph[tmpy][tmpx] == 1:
                visited[tmpy][tmpx] = True                
                dq.append([tmpx, tmpy, cnt+1])            
bfs(0, 0)