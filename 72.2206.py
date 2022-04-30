from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
vis = [[[False]*2 for _ in range(M)] for _ in range(N)]
def bfs(x, y):
    xpos = [0, 0, -1, 1]
    ypos = [-1, 1, 0, 0]
    q = deque([])
    q.append([x, y, 0])
    vis[y][x][0] = 1
    while q:
        xx, yy, cnt = q.popleft()
        if xx == M-1 and yy == N-1:
            print(vis[yy][xx][cnt])
            return
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < M and 0 <= tmpy < N and vis[tmpy][tmpx][cnt] == False:
                if graph[tmpy][tmpx] == 1 and cnt == 0:
                    vis[tmpy][tmpx][1] = vis[yy][xx][0] + 1
                    q.append([tmpx, tmpy, 1])
                if graph[tmpy][tmpx] == 0:
                    vis[tmpy][tmpx][cnt] = vis[yy][xx][cnt] + 1
                    q.append([tmpx, tmpy, cnt])
    print(-1)
bfs(0, 0)