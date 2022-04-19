# https://www.acmicpc.net/problem/7576
from collections import deque
M, N = map(int, input().split())
graph = []
for i in range(N):
    tlist = list(map(int, input().split()))
    graph.append(tlist)

visited = [ [False]*M for _ in range(N)]

def bfs(x, y):
    dx = [0, 0 , 1, -1]
    dy = [1, -1, 0, 0]    
    dq = deque([])

    for n in range(N):
        for m in range(M):
            if graph[n][m] == 1:
                dq.append([m, n, 0])
                visited[n][m] = True
    result = 0
    while dq:
        xx, yy, cnt = dq.popleft()                
        result = max(result, cnt)
        for i in range(4):
            tmpx = xx+dx[i]
            tmpy = yy+dy[i]

            if 0<=tmpx<M and 0<=tmpy<N and visited[tmpy][tmpx] is False and graph[tmpy][tmpx] == 0:
                visited[tmpy][tmpx] = True                
                graph[tmpy][tmpx] = 1
                dq.append([tmpx, tmpy, cnt+1])   
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                print(-1)
                return
    print(result)
bfs(0, 0)    
         

