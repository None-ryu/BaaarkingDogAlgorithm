N = int(input())
graph = [["*"]*N for _ in range(N)]
def star(stx, sty, K):
    if K == 1:
        return
    for i in range(K//3):
        tmpy = sty + K//3 + i
        for j in range(K//3):
            tmpx = stx + K//3 + j
            graph[tmpy][tmpx] = " "
    for i in range(sty, sty+K):
        if i == 0 or i%(K//3) == 0:
            newy = i
            for j in range(stx, stx+K):
                if j == 0 or j%(K//3) == 0:
                    newx = j
                    star(newx, newy, K//3)    
star(0, 0, N)
for i in graph:
    print(*i, sep="")