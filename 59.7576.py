from collections import deque
INF = int(1e9)
M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
vis = [[INF]*M for _ in range(N)]
xpos = [0, 0, 1, -1]
ypos = [1, -1, 0, 0]
def bfs(tom):
    q = deque([])
    for i in range(tom):
        q.append(ripe[i])
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < M and 0 <= tmpy < N and vis[tmpy][tmpx] == INF and graph[tmpy][tmpx] == 0:
                vis[tmpy][tmpx] = vis[yy][xx] + 1
                q.append((tmpx, tmpy))
    day = 0
    for i in range(N):
        for j in range(M):
            if vis[i][j] > day:
                day = vis[i][j]
    if day != INF:
        print(day)
    else:
        print(-1)
ripe = []
tomato = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            ripe.append((j, i))
            vis[i][j] = 0
            tomato += 1
        if graph[i][j] == -1:
            vis[i][j] = 0
bfs(tomato)