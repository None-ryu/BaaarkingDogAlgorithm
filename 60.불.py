# https://www.acmicpc.net/problem/4179
from collections import deque

R, C= map(int, input().split())
graph = []
for i in range(R):
    graph.append(list(input()))
visited = [ [False]*C for _ in range(R)]

# 출발점 먼저저장, 불좌표 저장
def bfs():
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    dq = deque()

    for r in range(R):
        for c in range(C):            
            if graph[r][c] == "F":
                dq.append([c, r, 'F', 1]) # 불먼저
                visited[r][c] = True
    for r in range(R):
        for c in range(C):            
            if graph[r][c] == "J":
                dq.append([c, r, '.', 1]) # 이동
                visited[r][c] = True    
    
    flag = False
    while dq:
        xx, yy, kind, cnt = dq.popleft()
        if kind=="." and (xx==C-1 or yy==R-1 or xx==0 or yy==0):
            print(cnt)
            flag = True
            break
        for i in range(4):
            tmpx = xx + dx[i]
            tmpy = yy + dy[i]
            
            if 0<=tmpx<C and 0<=tmpy<R and visited[tmpy][tmpx] is False and graph[tmpy][tmpx] == '.':
                if kind == 'F':
                    visited[tmpy][tmpx] = True
                    graph[tmpy][tmpx] = 'F'
                    dq.append([tmpx, tmpy, 'F', cnt+1])
                elif kind == '.':
                    visited[tmpy][tmpx] = True
                    dq.append([tmpx, tmpy, '.', cnt+1])
    if flag is False:
        print("IMPOSSIBLE")

bfs()