from collections import deque
N = int(input())
result = []
def bfs(x, y):
    xpos = [1, -1, 0, 0]
    ypos = [0, 0, 1, -1]
    q = deque([])
    cnt = 0
    q.append([x, y])
    graph[y][x] = 0
    cnt += 1
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < N and 0 <= tmpy < N and graph[tmpy][tmpx] == 1:
                graph[tmpy][tmpx] = 0
                cnt += 1
                q.append([tmpx, tmpy])
    result.append(cnt)
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(j, i)
print(len(result))
result.sort()
for i in result:
    print(i)