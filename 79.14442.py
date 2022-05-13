from collections import deque
import sys
N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
vis = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]
q = deque([])
xpos = [1, -1, 0, 0]
ypos = [0, 0, -1, 1]
q.append([0, 0, 0])
vis[0][0][0] = 1
while q:
    x, y, cnt = q.popleft()
    if x == M-1 and y == N-1:
        print(vis[y][x][cnt])
        sys.exit()
    for i in range(4):
        xx = x + xpos[i]
        yy = y + ypos[i]
        if 0 <= xx < M and 0 <= yy < N:
            if graph[yy][xx] == 0 and vis[yy][xx][cnt] == False:
                vis[yy][xx][cnt] = vis[y][x][cnt]+1
                q.append([xx, yy, cnt])
            elif graph[yy][xx] == 1 and cnt < K and vis[yy][xx][cnt+1] == False:
                vis[yy][xx][cnt+1] = vis[y][x][cnt]+1
                q.append([xx, yy, cnt+1])
print(-1)