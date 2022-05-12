from collections import deque
import sys
N, K = map(int, input().split())
vis = [False]*100001
def bfs(start, cnt):
    spos = [-1, 1]
    q = deque([])
    q.append([start, cnt])
    vis[start] = True
    while q:
        st, ct = q.popleft()
        if st == K:
            print(ct)
            sys.exit()
        for i in range(2):
            tmpst = st + spos[i]
            if 0 <= tmpst < 100001 and vis[tmpst] == False:
                vis[tmpst] = True
                q.append([tmpst, ct+1])
            if 0 <= st*2 < 100001 and vis[st*2] == False:
                vis[st*2] = True
                q.appendleft([st*2, ct])
bfs(N, 0)