from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
vis = []
for i in range(n):
    vis.append([False]*m)
xpos = [0, 0, 1, -1]
ypos = [1, -1, 0, 0]
result = []
def bfs(x, y):
    res = 0
    q = deque([])
    q.append([x, y])
    vis[y][x] = True
    res += 1
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < m and 0 <= tmpy < n and vis[tmpy][tmpx] is False and graph[tmpy][tmpx] == 1:
                vis[tmpy][tmpx] = True
                res += 1
                q.append([tmpx, tmpy])
    result.append(res)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and vis[i][j] is False:
            bfs(j, i)
print(len(result))
if len(result) != 0:
    print(max(result))
else:
    print(0)