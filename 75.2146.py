from collections import deque
INF = int(1e9)
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
vis = [[0]*N for _ in range(N)]
def bfs(x, y):
    global cnt
    q = deque([])
    q.append([x, y])
    graph[y][x] = cnt
    vis[y][x] = -1
    xpos = [1, -1, 0, 0]
    ypos = [0, 0, 1, -1]
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < N and 0 <= tmpy < N and vis[tmpy][tmpx] == 0 and graph[tmpy][tmpx] != 0:
                graph[tmpy][tmpx] = cnt
                vis[tmpy][tmpx] = -1
                q.append([tmpx, tmpy])
    cnt += 1
cnt = 1              
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and vis[i][j] == 0:
            bfs(j, i)
def findbfs(x, y):
    ted = [[0]*N for _ in range(N)]
    global way
    stx = x
    sty = y
    q = deque([])
    q.append([x, y])
    xpos = [1, -1, 0, 0]
    ypos = [0, 0, 1, -1]
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < N and 0 <= tmpy < N and ted[tmpy][tmpx] == 0 and graph[tmpy][tmpx] != graph[sty][stx]:
                if graph[tmpy][tmpx] != 0:
                    if ted[yy][xx] < way:
                        way = ted[yy][xx]
                    return
                ted[tmpy][tmpx] = ted[yy][xx] + 1
                q.append([tmpx, tmpy])
way = INF
for i in range(N):
    for j in range(N):
        if vis[i][j] == -1:
            findbfs(j, i)
print(way)
# for i in graph:
#     print(i)
# print("-----------------")
# for i in vis:
#     print(i)