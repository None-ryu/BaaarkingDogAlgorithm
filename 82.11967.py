from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[False]*N for _ in range(N)]
vis = [[False]*N for _ in range(N)]
switch = []
for _ in range(M):
    switch.append(list(map(int, input().split())))
xpos = [0, 0, 1, -1]
ypos = [1, -1, 0, 0]
q = deque([])
q.append([0, 0])
graph[0][0] = True
vis[0][0] = True
cnt = 1
while q:
    x, y = q.popleft()
    for i in range(len(switch)):
        if x == switch[i][1]-1 and y == switch[i][0]-1 and graph[switch[i][2]-1][switch[i][3]-1] == False:
            graph[switch[i][2]-1][switch[i][3]-1] = True
            cnt += 1
            for j in range(4):
                tmpx = switch[i][3]-1 + xpos[j]
                tmpy = switch[i][2]-1 + ypos[j]
                if 0 <= tmpx < N and 0 <= tmpy < N and vis[tmpy][tmpx] == True:
                    vis[switch[i][2]-1][switch[i][3]-1] = True
                    q.append([switch[i][3]-1, switch[i][2]-1])
                    for k in range(4):
                        tmpx = switch[i][3]-1 + xpos[k]
                        tmpy = switch[i][2]-1 + ypos[k]
                        if 0 <= tmpx < N and 0 <= tmpy < N and graph[tmpy][tmpx] == True and vis[tmpy][tmpx] == False:
                            vis[tmpy][tmpx] = True
                            q.append([tmpx, tmpy])
    for i in range(4):
        xx = x + xpos[i]
        yy = y + ypos[i]
        if 0 <= xx < N and 0 <= yy < N:
            if graph[yy][xx] == True and vis[yy][xx] == False:
                vis[yy][xx] = True
                q.append([xx, yy])
print(cnt)