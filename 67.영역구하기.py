# https://www.acmicpc.net/problem/2583
from collections import deque

M, N, K = map(int, input().split())
graph = [ [0]*N for _ in range(M) ]
for i in range(K):
    sx, sy, ex, ey = map(int, input().split())
    
    for y in range(sy, ey):
        for x in range(sx, ex):
            graph[y][x] = 1

# for i in graph:
#     print(i)
# [0, 0, 0, 0, 1, 1, 0]
# [0, 1, 0, 0, 1, 1, 0]
# [1, 1, 1, 1, 0, 0, 0]
# [1, 1, 1, 1, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0]
result = []
def bfs(x, y):
    posx = [0,0,1,-1]
    posy = [1,-1, 0,0]
    dq = deque()
    dq.append([x, y])
    graph[y][x] = 2
    cnt = 1
    while dq:
        tmpx, tmpy = dq.popleft()
        for i in range(4):
            xx = tmpx + posx[i]
            yy = tmpy + posy[i]

            if 0<=xx<N and 0<=yy<M and graph[yy][xx]==0:
                graph[yy][xx] = 2
                dq.append([xx, yy])
                cnt += 1
    result.append(cnt)

for y in range(M):
    for x in range(N):
        if graph[y][x] == 0:
            bfs(x, y)


print(len(result))
result.sort()
print(*result)