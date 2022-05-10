from collections import deque
import copy
import sys
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
def bfs(x, y):
    global graph
    global cnt
    global able
    vis = [[False]*M for _ in range(N)]
    melted = copy.deepcopy(graph)
    q = deque([])
    q.append([x, y])
    xpos = [1, -1, 0, 0]
    ypos = [0, 0, 1, -1]
    while q:
        xx, yy = q.popleft()
        water = 0
        for i in range(4):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < M and 0 <= tmpy < N and vis[tmpy][tmpx] == False:
                if graph[tmpy][tmpx] != 0:
                    vis[tmpy][tmpx] = True
                    q.append([tmpx, tmpy])
                else:
                    water += 1
        if graph[yy][xx] - water >= 0:
            melted[yy][xx] = graph[yy][xx] - water
        else:
            melted[yy][xx] = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and vis[i][j] == False:
                print(cnt)
                able = True
                sys.exit()
    graph = copy.deepcopy(melted)
cnt = 0
able = False                
while True:
    total = 0
    for i in graph:
        total += sum(i)
    if total == 0 and able == False:
        print(0)
        break
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                bfs(j, i)
                cnt += 1