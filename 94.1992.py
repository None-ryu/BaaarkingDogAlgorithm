N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
result = ""
def section(stx, sty, K):
    tmpx = -1
    tmpy = -1
    for i in range(sty, sty+K):
        if i == 0 or i%(K//2) == 0:
            tmpy = i
            for j in range(stx, stx+K):
                if j == 0 or j%(K//2) == 0:
                    tmpx = j
                    color(tmpx, tmpx+K//2, tmpy, tmpy+K//2, K//2)
def color(stx, edx, sty, edy, K):
    global result
    flag = False
    for i in range(sty, edy):
        for j in range(stx, edx):
            if graph[i][j] != graph[sty][stx]:
                flag = True
                result += "("
                section(stx, sty, K)
                result += ")"
                return
    if flag == False:
        result += str(graph[sty][stx])
color(0, N, 0, N, N)
print(result)