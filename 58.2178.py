from collections import deque
INF = int(1e9)
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
vis = [[INF]*M for _ in range(N)]
xpos = [0, 0, 1, -1]
ypos = [1, -1, 0, 0]
def bfs(x, y):
    q = deque([])
    q.append([x, y])
    vis[y][x] = True
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < M and 0 <= tmpy < N and graph[tmpy][tmpx] == 1 and vis[tmpy][tmpx] == INF:
                vis[tmpy][tmpx] = vis[yy][xx] + 1
                q.append((tmpx, tmpy))
    print(vis[N-1][M-1])
bfs(0, 0)