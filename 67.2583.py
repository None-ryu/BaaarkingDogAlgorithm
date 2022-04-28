from collections import deque
M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
for _ in range(K):
    stx, sty, edx, edy = map(int, input().split())
    for i in range(edx-stx):
        for j in range(edy-sty):
            graph[sty+j][stx+i] = 1
def bfs(x, y):
    q = deque([])
    cnt = 0
    q.append([x, y])
    graph[y][x] = 1
    cnt += 1
    xpos = [1, -1, 0, 0]
    ypos = [0, 0, 1, -1]
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < N and 0 <= tmpy < M and graph[tmpy][tmpx] == 0:
                graph[tmpy][tmpx] = 1
                cnt += 1
                q.append([tmpx, tmpy])
    result.append(cnt)
result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            bfs(j, i)
print(len(result))
print(*sorted(result))