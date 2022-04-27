from collections import deque
def bfs(x, y):
    xpos = [-2, -1, 1, 2, -2, -1, 1, 2]
    ypos = [-1, -2, -2, -1, 1, 2, 2, 1]
    q = deque([])
    q.append([x, y])
    while q:
        xx, yy = q.popleft()
        if xx == endx and yy == endy:
            break
        for i in range(8):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < I and 0 <= tmpy < I and vis[tmpy][tmpx] is False:
                vis[tmpy][tmpx] = vis[yy][xx] + 1
                q.append([tmpx, tmpy])
case = int(input())
for _ in range(case):
    I = int(input())
    nowx, nowy = map(int, input().split())
    endx, endy = map(int, input().split())
    vis = [[False]*I for _ in range(I)]
    vis[nowy][nowx] = 0
    bfs(nowx, nowy)
    print(vis[endy][endx])