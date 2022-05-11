# https://www.acmicpc.net/problem/2146
from collections import deque
import sys
import copy

# 입력값 받기
N = int(input())
graph = []
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

# 넘버링
def bfs(x, y, cnt):
    global graph
    dq = deque([])
    dq.append([x, y])
    graph[y][x] = cnt
    
    posx = [0,0,1,-1]
    posy = [1,-1,0,0]
    while dq:
        tmpx, tmpy = dq.popleft()
        for i in range(4):
            xx = tmpx+posx[i]
            yy = tmpy+posy[i]

            if 0<=xx<N and 0<=yy<N and graph[yy][xx] == 1:
                graph[yy][xx] = cnt
                dq.append([xx, yy])

cnt = 1
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            cnt+=1
            bfs(x, y, cnt)


# for y in graph:
#     print(y)

# bfs로 새로운 영토에 도달하는 순간 체크
result = 1000
def getBFS(x, y, areaNum):
    flag = False
    global result
    ted = [[0]*N for _ in range(N)]
    ted[y][x] = 1
    ckdq = deque([])
    ckdq.append([x, y, areaNum, 0])
    posx = [0,0,1,-1]
    posy = [1,-1,0,0]
    while ckdq:
        tmpx, tmpy, num, cnt = ckdq.popleft()
        for i in range(4):
            xx = tmpx+posx[i]
            yy = tmpy+posy[i]

            
            if 0<=xx<N and 0<=yy<N and ted[yy][xx]==0:
                # 0인 경우에만(가운데는 상관없기 때문에 가에만 체크)
                ted[yy][xx] = 1
                if graph[yy][xx] == 0:            
                    ckdq.append([xx, yy, num, cnt+1])            
                if graph[yy][xx] > 0 and graph[yy][xx] != num:            
                    result = min(result, cnt)
                    flag = True                    
        if flag is True:
            break
                 


for y in range(N):
    for x in range(N):
        if graph[y][x] > 0:
            getBFS(x, y, graph[y][x])

print(result)
















"""

# https://www.acmicpc.net/problem/2146
from collections import deque
import sys

# 입력값 받기
N = int(input())
graph = []
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

# 넘버링
def bfs(x, y, cnt):
    global graph
    dq = deque([])
    dq.append([x, y])
    graph[y][x] = cnt
    posx = [0,0,1,-1]
    posy = [1,-1,0,0]
    while dq:
        tmpx, tmpy = dq.popleft()
        for i in range(4):
            xx = tmpx+posx[i]
            yy = tmpy+posy[i]

            if 0<=xx<N and 0<=yy<N and graph[yy][xx] == 1:
                graph[yy][xx] = cnt
                dq.append([xx, yy])

cnt = 1
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            cnt+=1
            bfs(x, y, cnt)

# for y in graph:
#     print(y)


# bfs로 새로운 영토에 도달하는 순간 체크
result = 10000
def getBfs(areaNum):
    ted = [[0]*N for _ in range(N)]
    global result
    flag = False
    ckdq = deque([])
    posx = [0,0,1,-1]
    posy = [1,-1,0,0]              

    for y in range(N):
        for x in range(N):
            if graph[y][x] == areaNum:
                ckdq.append([x, y, 0])      
                ted[y][x] = 1
    while ckdq:
        tmpx, tmpy, cnt = ckdq.popleft()
        for i in range(4):
            xx = tmpx+posx[i]
            yy = tmpy+posy[i]
            
            if 0<=xx<N and 0<=yy<N and ted[yy][xx] == 0:
                ted[yy][xx] == 1
                # 0인 경우에만(가운데는 상관없기 때문에 가에만 체크)
                if graph[yy][xx] == 0:            
                    ckdq.append([xx, yy, cnt+1])            
                if graph[yy][xx] > 0 and graph[yy][xx] != areaNum:            
                    flag = True
                    result = min(result, cnt)
                    break
        if flag is True:
            break

# 2-3 연결하는것과 3-2 연결하는것이 중복되서 ckdq에 쌓이면 안됨 2번땅부터 탐색 후 3번 땅 체크
for i in range(2, cnt+1):
    getBfs(i)
print(result)
"""