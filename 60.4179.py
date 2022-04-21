from collections import deque
INF = int(1e9)
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))
vis = [[INF]*C for _ in range(R)]
xpos = [0, 0, -1, 1]
ypos = [-1, 1, 0, 0]
def bfs():
    flag = False
    q = deque([])
    for i in start:
        q.append(i)
        vis[i[1]][i[0]] = 0
    while q:
        x, y = q.popleft()
        if y == R-1 or x == C-1 or y == 0 or x == 0:
            if graph[y][x] == "." or graph[y][x] == "J":
                flag = True
                print(vis[y][x]+1)
                break
        for i in range(4):
            tmpx = x + xpos[i]
            tmpy = y + ypos[i]
            if 0 <= tmpx < C and 0 <= tmpy < R and vis[tmpy][tmpx] == INF and graph[tmpy][tmpx] == ".":
                if graph[y][x] == "F":
                    vis[tmpy][tmpx] = 0
                    graph[tmpy][tmpx] = "F"
                    q.append((tmpx, tmpy))
                else:
                    vis[tmpy][tmpx] = vis[y][x] + 1
                    q.append((tmpx, tmpy))
    if flag == False:
        print("IMPOSSIBLE")
start = deque([])
for i in range(R):
    for j in range(C):
        if graph[i][j] == "J":
            start.append((j, i))
        if graph[i][j] == "F":
            start.appendleft((j, i))
        if graph[i][j] == "#":
            vis[i][j] = 0
bfs()