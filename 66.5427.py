from collections import deque
case = int(input())
def bfs():
    global q
    xpos = [0, 0, 1, -1]
    ypos = [1, -1, 0, 0]
    able = 0
    while q:
        x, y = q.popleft()
        if x == 0 or x == w-1 or y == 0 or y == h-1:
            if graph[y][x] == "@":
                print(vis[y][x]+1)
                able = 1
                break
        for i in range(4):
            xx = x + xpos[i]
            yy = y + ypos[i]
            if 0 <= xx < w and 0 <= yy < h and graph[yy][xx] == ".":
                if graph[y][x] == "*":
                    graph[yy][xx] = "*"
                    q.append([xx, yy])
                else:
                    graph[yy][xx] = "@"
                    vis[yy][xx] = vis[y][x] + 1
                    q.append([xx, yy])
    if able == 0:
        print("IMPOSSIBLE")
for _ in range(case):
    w, h = map(int, input().split())
    graph = []
    for _ in range(h):
        graph.append(list(input()))
    vis = [[False]*w for _ in range(h)]
    q = deque([])
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "@":
                vis[i][j] = 0
                q.append([j, i])
            if graph[i][j] == "*":
                q.appendleft([j, i])
    bfs()