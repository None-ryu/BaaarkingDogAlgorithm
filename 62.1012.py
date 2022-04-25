from collections import deque
T = int(input())
def bfs(x, y):
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
            if 0 <= tmpx < M and 0 <= tmpy < N and vis[tmpy][tmpx] is False and graph[tmpy][tmpx] == 1:
                vis[tmpy][tmpx] = True
                q.append([tmpx, tmpy])
    result += 1
for _ in range(T):
    result = 0
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    vis = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and vis[i][j] is False:
                bfs(j, i)
    print(result)