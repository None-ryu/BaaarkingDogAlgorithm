# https://www.acmicpc.net/problem/5014
from collections import deque

F, S, G, U, D = map(int, input().split())    

visited = [0] * (F+1)

def bfs(x):
    pos = [U, D*-1]
    dq = deque()
    dq.append([x, 0])
    visited[x] = 1
    
    flag = False
    while dq:
        tmpx, cnt = dq.popleft()
        if tmpx == G:
            print(cnt)
            flag = True
            break
        for i in range(2):
            xx = tmpx + pos[i]
            if 0<xx<=F and visited[xx]==0:
                visited[xx] = 1
                dq.append([xx, cnt+1])                    
    if flag is False:
        print("use the stairs")
bfs(S) # 지금 있는 곳