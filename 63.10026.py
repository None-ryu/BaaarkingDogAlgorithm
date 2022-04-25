from collections import deque
N = int(input())
def bfs1(x, y):
    global result
    xpos = [0, 0, 1, -1]
    ypos = [1, -1, 0, 0]
    q = deque([])
    q.append([x, y])
    vis[y][x] = True
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < N and 0 <= tmpy < N and vis[tmpy][tmpx] is False and graph[tmpy][tmpx] == graph[yy][xx]:
                vis[tmpy][tmpx] = True
                q.append([tmpx, tmpy])
    result += 1
    for i in range(N):
        for j in range(N):
            if vis[j][i] == False:
                bfs1(i, j)
def bfs2(x, y):
    global RGresult
    global Bresult
    state = 0
    xpos = [0, 0, 1, -1]
    ypos = [1, -1, 0, 0]
    q = deque([])
    q.append([x, y])
    vis[y][x] = True
    while q:
        xx, yy = q.popleft()
        if graph[yy][xx] == "R" or graph[yy][xx] == "G":
            state = "RG"
        if graph[yy][xx] == "B":
            state = "B"
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < N and 0 <= tmpy < N and vis[tmpy][tmpx] is False and str(graph[tmpy][tmpx]) in state:
                vis[tmpy][tmpx] = True
                q.append([tmpx, tmpy])
    if state == "RG":
        RGresult += 1
    if state == "B":
        Bresult += 1
    for i in range(N):
        for j in range(N):
            if vis[j][i] == False:
                bfs2(i, j)
graph = []
for _ in range(N):
    graph.append(list(input()))
vis = [[False]*N for _ in range(N)]
result = 0
bfs1(0, 0)
vis = [[False]*N for _ in range(N)]
RGresult = 0
Bresult = 0
bfs2(0, 0)
print(result, RGresult+Bresult)