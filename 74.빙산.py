# https://www.acmicpc.net/problem/2573
from collections import deque
import sys
import copy
N, M = map(int, input().split())
graph = []
dq = deque()
dq2 = deque()
for fy in range(N):
    tmplist = list(map(int, input().split())) 
    graph.append(tmplist)
    for fx in range(len(tmplist)):
        if graph[fy][fx] > 0:
            dq.append([fx, fy])

posx = [0,0,1,-1]
posy = [1,-1,0,0]

result = 0
while True:
    print("--------------")
    result += 1
    #큐에 있는 모든 좌표의 사방탐색 후 빙산 녹이기 
    graphcopy = copy.deepcopy(graph)
    
    while dq:
        xx, yy = dq.popleft()
        water = 0
        for i in range(4):
            tmpx = xx+posx[i]
            tmpy = yy+posy[i]
            if graph[tmpy][tmpx] == 0:
                water += 1
        if water > 0 :
            if graph[yy][xx]<= water:
                graphcopy[yy][xx] = 0                
            else:    
                graphcopy[yy][xx] = graph[yy][xx]-water
        
        if graphcopy[yy][xx] > 0:
            dq2.append([xx, yy]) # 0보다 크면 빙산임 영역갯수 체크 위해 필요
    graph = copy.deepcopy(graphcopy)
    # 빙산의 합을 구한다
    total = 0
    for y in graph:
        total += sum(y)
    if total <= 0:
        print(0)
        sys.exit()
    # bfs로 체크
    visited = [ [False]*M  for _ in range(N)]
    area = 0
    while dq2:
        xx, yy = dq2.popleft()
        if visited[yy][xx] is True:
            continue
        if graph[yy][xx] == 0:
            continue
        dq3 = deque()
        dq3.append([xx, yy])
        area += 1
        while dq3:
            xx, yy = dq3.popleft()
        for i in range(4):
            tmpx = xx+posx[i]
            tmpy = yy+posy[i]
            if 0<=tmpx<M and 0<=tmpy<N and visited[tmpy][tmpx] is False and graph[tmpy][tmpx] > 0:
                visited[tmpy][tmpx] = True
    
    if area >= 2:
        print(result)
        sys.exit()
print(graph)