# https://www.acmicpc.net/problem/10026
from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append( list(input()) )
visited = [[False] * N for _ in range(N)]
def bfs(x, y, color):
    pox = [0,0,1,-1]
    poy = [1,-1,0,0]
    dq = deque()
    dq.append([x, y])
    visited[y][x] = True
    while dq:
        xx, yy = dq.popleft()
        for i in range(4):
            tmpx = xx+pox[i]
            tmpy = yy+poy[i]
            if 0<=tmpx<N and 0<=tmpy<N and graph[tmpy][tmpx] == color and visited[tmpy][tmpx] is False:
                visited[tmpy][tmpx] = True
                dq.append([tmpx, tmpy])
cnt = 0
for y in range(N):
    for x in range(N):
        if visited[y][x] is False:
            bfs(x, y, graph[y][x])
            cnt+=1

for y in range(N):
    for x in range(N):
        if graph[y][x] == 'G':
            graph[y][x]= 'R'

blindVisited = [[False] * N for _ in range(N)]
def blindbfs(x, y, color):
    pox = [0,0,1,-1]
    poy = [1,-1,0,0]
    dq = deque()
    dq.append([x, y])
    blindVisited[y][x] = True
    
    while dq:
        xx, yy = dq.popleft()
        for i in range(4):
            tmpx = xx+pox[i]
            tmpy = yy+poy[i]
            if 0<=tmpx<N and 0<=tmpy<N and graph[tmpy][tmpx] == color and blindVisited[tmpy][tmpx] is False:
                blindVisited[tmpy][tmpx] = True
                dq.append([tmpx, tmpy])

ncnt = 0
for y in range(N):
    for x in range(N):
        if blindVisited[y][x] is False:
            blindbfs(x, y, graph[y][x])
            ncnt +=1
print(cnt, ncnt)