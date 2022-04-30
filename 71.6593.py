from collections import deque
INF = int(1e9)
def bfs():
    able = 0
    xpos = [0, 0, 1, -1, 0, 0]
    ypos = [1, -1, 0, 0, R, -R]
    q = deque([])
    for i in range(L*R):
        for j in range(C):
            if graph[i][j] == "S":
                q.append([j, i])
                vis[i][j] = 0
    while q:
        x, y = q.popleft()
        if graph[y][x] == "E":
            able = 1
            break
        for i in range(6):
            xx = x + xpos[i]
            yy = y + ypos[i]
            if y%R == R-1 and yy%R == 0:
                continue
            if y%R == 0 and yy%R == R-1:
                continue
            if 0 <= xx < C and 0 <= yy < L*R and vis[yy][xx] == INF and graph[yy][xx] != "#":
                vis[yy][xx] = vis[y][x] + 1
                q.append([xx, yy])
    if able == 1:
        print("Escaped in", vis[y][x], "minute(s).", sep=" ")
    else:
        print("Trapped!")
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    graph = []
    vis = [[INF]*C for _ in range(L*R)]
    for i in range((R+1)*L):
        arr = list(input())
        if (i+1)%(R+1) != 0:
            graph.append(arr)
    bfs()