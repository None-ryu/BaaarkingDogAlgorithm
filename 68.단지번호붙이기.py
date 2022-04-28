# https://www.acmicpc.net/problem/2667
from collections import deque

S = int(input())
graph = []
for i in range(S):
    graph.append(list(map(int, list(input()))))
    
# for i in graph:
#     print(i)

result = []
def bfs(x, y):
    posx = [0,0,1,-1]
    posy = [1,-1, 0,0]
    dq = deque()
    dq.append([x, y])
    graph[y][x] = 2 # 집 카운팅 완료
    cnt = 1
    while dq:
        tmpx, tmpy = dq.popleft()
        for i in range(4):
            xx = tmpx + posx[i]
            yy = tmpy + posy[i]

            if 0<=xx<S and 0<=yy<S and graph[yy][xx]==1:
                graph[yy][xx] = 2
                dq.append([xx, yy])
                cnt += 1
    result.append(cnt)

for y in range(S):
    for x in range(S):
        if graph[y][x] == 1:
            bfs(x, y)

print(len(result))
result.sort()
for i in result:
    print(i)