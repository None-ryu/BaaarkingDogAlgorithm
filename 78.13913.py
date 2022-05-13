# from collections import deque
# import sys
# N, K = map(int, input().split())
# vis = [False]*100001
# def bfs(start, cnt):
#     spos = [-1, 1, 2]
#     q = deque([])
#     q.append([start, cnt])
#     vis[start] = True
#     while q:
#         st, ct = q.popleft()
#         if st == K:
#             print(ct)
#             result = str(st)
#             after = st
#             while True:
#                 if after == start:
#                     break
#                 after = vis[after]
#                 result = str(after) + " " + result
#             print(result)
#             sys.exit()
#         for i in range(3):
#             if i < 2:
#                 tmpst = st + spos[i]
#             else:
#                 tmpst = st*spos[i]
#             if 0 <= tmpst < 100001 and vis[tmpst] == False:
#                 vis[tmpst] = st
#                 q.append([tmpst, ct+1])
# bfs(N, 0)

from collections import deque
import sys
N, K = map(int, input().split())
vis = [False]*100001
def bfs(start, cnt, way):
    spos = [-1, 1, 2]
    q = deque([])
    q.append([start, cnt, way])
    vis[start] = True
    while q:
        st, ct, wy = q.popleft()
        if st == K:
            print(ct)
            print(wy)
            sys.exit()
        for i in range(3):
            if i < 2:
                tmpst = st + spos[i]
            else:
                tmpst = st*spos[i]
            if 0 <= tmpst < 100001 and vis[tmpst] == False:
                vis[tmpst] = st
                q.append([tmpst, ct+1, wy+" "+str(tmpst)])
bfs(N, 0, str(N))