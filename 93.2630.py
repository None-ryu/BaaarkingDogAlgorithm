N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
a = 0
b = 0
def section(stx, sty, K):
    for i in range(sty, sty+K):
        if i == 0 or i%(K//2) == 0:
            tmpy = i
            for j in range(stx, stx+K):
                if j == 0 or j%(K//2) == 0:
                    tmpx = j
                    color(tmpx, tmpx+K//2, tmpy, tmpy+K//2, K//2)
def color(stx, edx, sty, edy, K):
    global a
    global b
    if K == 1:
        if graph[sty][stx] == 0:
            a += 1
        elif graph[sty][stx] == 1:
            b += 1
        return
    flag = False
    for i in range(sty, edy):
        for j in range(stx, edx):
            if graph[i][j] != graph[sty][stx]:
                flag = True
                section(stx, sty, K)
                return
    if flag == False:
        if graph[sty][stx] == 0:
            a += 1
        elif graph[sty][stx] == 1:
            b += 1
color(0, N, 0, N, N)
print(a)
print(b)