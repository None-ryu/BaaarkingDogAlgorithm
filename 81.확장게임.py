# https://www.acmicpc.net/problem/16920
from collections import deque
import sys
import copy
input = sys.stdin.readline

N, M, P = map(int, input().split())
movcnt = [0] + list(map(int, input().split())) # [0, 1, 1, 1, 1]
area = [[] for _ in range(P+1)] # [x] [] [] [] []
result = [0]*(P+1)

graph = []
for i in range(N):
    tmp = list(input())
    graph.append(tmp)

def func(mydq, num):
    mydq = deque(mydq)
    tmp = 0
    global total
    posx = [0,0,1,-1]
    posy = [1,-1,0,0]
    
    newdq = deque([])
    while mydq:
        tmpx, tmpy = mydq.popleft()     
      
        for i in range(4):
            xx = tmpx+posx[i]
            yy = tmpy+posy[i]

            if 0<=xx<M and 0<=yy<N:
                if graph[yy][xx] == '.':
                    graph[yy][xx] = num
                    total += 1
                    tmp += 1
                    result[num] += 1
                    newdq.append([xx, yy]) 
    area[num] = copy.deepcopy(newdq)
    return tmp

def bfs(num):
    tmp = 0
    cnt = 0
    for i in range(movcnt[num]):
        cnt += 1
        dq = area[num] # [(0,1),(0,2), (0,3)]
        tmp += func(dq, num)
        if len(area[num]) == 0:
            break
    return tmp

total = 0
for y in range(N):
    for x in range(M):
        # 숫자인 경우
        if graph[y][x] != '.'  and graph[y][x] != '#':
            tmpNum = int(graph[y][x])
            area[tmpNum].append([x, y])
            total += 1
            result[tmpNum] += 1
        if graph[y][x] == '#':
            total += 1
while total < N*M:
    flag = False
    for i in range(1, P+1):
        if bfs(i) > 0:
            flag = True
    if flag is False:
        break

for i in graph:
    print(i)

for i in range(1, len(result)):
    print(result[i], end=" ")
    

