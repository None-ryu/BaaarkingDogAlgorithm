# https://www.acmicpc.net/problem/1012
import sys
from collections import deque
sys.setrecursionlimit(10000) 

T = int(input())

def bfs(graph, xx, yy, M, N):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    dq = deque([])
    dq.append([xx, yy])
    graph[yy][xx] = 2

    while dq:
        tmpx, tmpy = dq.popleft()
        for i in range(4):
            xx = tmpx+dx[i]
            yy = tmpy+dy[i]
            if 0<=xx<M and 0<=yy<N and graph[yy][xx]==1:
                graph[yy][xx] = 2
                dq.append([xx, yy])

def dfs(graph, xx, yy, M, N):    
    if 0<=xx<M and 0<=yy<N and graph[yy][xx]==1:
        graph[yy][xx] = 2
        dfs(graph, xx+1, yy, M, N)
        dfs(graph, xx-1, yy, M, N)
        dfs(graph, xx, yy+1, M, N)
        dfs(graph, xx, yy-1, M, N)

for i in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]

    for k in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for yy in range(N):
        for xx in range(M):
            if graph[yy][xx] == 1:
                dfs(graph, xx, yy, M, N)
                cnt += 1
    print(cnt)