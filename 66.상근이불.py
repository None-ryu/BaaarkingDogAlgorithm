# https://www.acmicpc.net/problem/5427
from collections import deque
N = int(input())

for i in range(N):
    w, h = map(int, input().split())
    graph = []
    for hc in range(h):
            graph.append(list(input()))
    visited = [ [False]*w for _ in range(h)]    
    stx, sty = -1, -1
    fire = []
    for hc in range(h):
        for wc in range(w):
            if graph[hc][wc] == '@':
                stx = wc
                sty = hc
            elif graph[hc][wc] == '*':
                fire.append([wc, hc])

    pox = [0,0,1,-1]
    poy = [1,-1, 0,0]
    dq = deque([])
    for x, y in fire:
        dq.append([x, y, '*', 1])
        visited[y][x] = True
    dq.append([stx, sty, '.', 1])
    visited[sty][stx] = True
    graph[sty][stx] = '.'
    
    checkPossible = False
    while dq:
        tmpx, tmpy, kind, cnt = dq.popleft()
        if kind == "." and (tmpx == 0 or tmpx == w-1 or tmpy == 0 or tmpy == h-1):
            checkPossible = True
            print(cnt)
            break
        for i in range(4):
            xx = tmpx+pox[i]
            yy = tmpy+poy[i]
            if 0<=xx<w and 0<=yy<h and visited[yy][xx] is False and graph[yy][xx] == '.':
                if kind == "*":
                    graph[yy][xx] = "*"
                    visited[yy][xx] = True
                    dq.append([xx, yy, kind, cnt+1])
                elif kind == ".":
                    visited[yy][xx] = True
                    dq.append([xx, yy, kind, cnt+1])
    
    if checkPossible is False:
        print("IMPOSSIBLE")