from collections import deque
import copy
N = int(input())
graph = []
est = 0
for _ in range(N):
    arr = list(map(int, input().split()))
    for i in arr:
        if i > est:
            est = i
    graph.append(arr)
def bfs(x, y):
    global cnt
    xpos = [1, -1, 0, 0]
    ypos = [0, 0, 1, -1]
    q = deque([])
    q.append([x, y])
    while q:
        xx, yy = q.popleft()
        rain[yy][xx] = 0
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < N and 0 <= tmpy < N and rain[tmpy][tmpx] > high:
                rain[tmpy][tmpx] = 0
                q.append([tmpx, tmpy])
    cnt += 1
high = 0
cnt = 0
result = []
for i in range(est):
    rain = copy.deepcopy(graph)
    high = i
    cnt = 0
    for j in range(N):
        for k in range(N):
            if rain[j][k] > high:
                bfs(k, j)
    result.append(cnt)
if len(result) != 0:
    print(max(result))
else:
    print(0)