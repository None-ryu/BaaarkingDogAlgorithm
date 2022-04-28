from collections import deque
INF = int(1e9)
F, S, G, U, D = map(int, input().split())
vis = [INF]*(F+1)
def bfs(st):
    q = deque([])
    able = 0
    q.append(st)
    vis[st] = 0
    UDpos = [-D, U]
    while q:
        start = q.popleft()
        if start == G:
            print(vis[start])
            able = 1
            break
        for i in range(2):
            move = start + UDpos[i]
            if 1 <= move <= F and vis[move] == INF:
                vis[move] = vis[start] + 1
                q.append(move)
    if able == 0:
        print("use the stairs")
bfs(S)