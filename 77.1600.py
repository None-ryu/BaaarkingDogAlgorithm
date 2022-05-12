# from collections import deque
# K = int(input())
# W, H = map(int, input().split())
# graph = []
# for _ in range(H):
#     graph.append(list(map(int, input().split())))
# vis = [[False]*W for _ in range(H)]
# def bfs(stx, sty, cnt):
#     able = False
#     q = deque([])
#     xpos = [-1, 1, 0, 0, -2, -1, 1, 2, -2, -1, 1, 2]
#     ypos = [0, 0, -1, 1, -1, -2, -2, -1, 1, 2, 2, 1]
#     vis[sty][stx] = 0
#     q.append([stx, sty, cnt])
#     while q:
#         xx, yy, ct = q.popleft()
#         if xx == W-1 and yy == H-1:
#             print(vis[yy][xx])
#             able = True
#             break
#         for i in range(12):
#             tmpx = xx + xpos[i]
#             tmpy = yy + ypos[i]
#             if 0 <= tmpx < W and 0 <= tmpy < H and vis[tmpy][tmpx] == False and graph[tmpy][tmpx] != 1:
#                 if i < 4:
#                     vis[tmpy][tmpx] = vis[yy][xx]+1
#                     q.append([tmpx, tmpy, ct])
#                 else:
#                     if ct < K:
#                         vis[tmpy][tmpx] = vis[yy][xx]+1
#                         q.append([tmpx, tmpy, ct+1])
#     if able == False:
#         print(-1)
# bfs(0, 0, 0)

from collections import deque
K = int(input())
W, H = map(int, input().split())
graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))
vis = [[[False]*(K+1) for _ in range(W)] for _ in range(H)]
def bfs(stx, sty, cnt):
    able = False
    q = deque([])
    xpos = [-1, 1, 0, 0, -2, -1, 1, 2, -2, -1, 1, 2]
    ypos = [0, 0, -1, 1, -1, -2, -2, -1, 1, 2, 2, 1]
    vis[sty][stx][cnt] = 0
    q.append([stx, sty, cnt])
    while q:
        xx, yy, ct = q.popleft()
        if xx == W-1 and yy == H-1:
            print(vis[yy][xx][ct])
            able = True
            break
        for i in range(12):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if 0 <= tmpx < W and 0 <= tmpy < H and graph[tmpy][tmpx] != 1:
                if i < 4:
                    if vis[tmpy][tmpx][ct] == False:
                        vis[tmpy][tmpx][ct] = vis[yy][xx][ct]+1
                        q.append([tmpx, tmpy, ct])
                else:
                    if ct < K and vis[tmpy][tmpx][ct+1] == False:
                        vis[tmpy][tmpx][ct+1] = vis[yy][xx][ct]+1
                        q.append([tmpx, tmpy, ct+1])
    if able == False:
        print(-1)
bfs(0, 0, 0)