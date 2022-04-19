# https://www.acmicpc.net/problem/1926
from collections import deque

N, M = map(int, input().split())
arr = []
visited = [ [False]*M for _ in range(N)]

for i in range(N):
    arr.append(list(map(int, input().split())))

def bfs(x, y):
    global visited
    global arr
    global N
    global M

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    dq = deque([])
    dq.append([x, y])
    visited[y][x] = True
    photoSize = 1
    while dq:
        tmpx, tmpy = dq.popleft()
        for i in range(4):
            xx = tmpx+dx[i]
            yy = tmpy+dy[i]
            if 0<=xx<M and 0<=yy<N and arr[yy][xx] == 1 and visited[yy][xx] is False:
                visited[yy][xx] = True
                dq.append([xx, yy])
                photoSize+=1
    return photoSize

maxPhoto = 0
photoCnt = 0
for n in range(N):
    for m in range(M):
        if arr[n][m] == 1 and visited[n][m] is False:
            maxPhoto = max(maxPhoto, bfs(m, n))
            photoCnt+=1
print(photoCnt)
print(maxPhoto)


# 반례
# 4 5
# 1 1 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 1 1