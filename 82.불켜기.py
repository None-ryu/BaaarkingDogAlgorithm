# https://www.acmicpc.net/problem/11967
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*N for _ in range(N)] # 0은 불 꺼져있음
visited = [[False]*N for _ in range(N)]
cnt = 1
switch = []

# {'1x1': '1x2,1x3', '2x1': '2x2', '2x3': '3x1', '1x3': '1x2,2x1'}

for i in range(M):
    x, y, a, b = map(int, input().split())    
    switch.append([x,y,a,b])
#print(dict)

def light(x, y):
    dq = deque([])
    posx = [0,0,1,-1]
    posy = [1,-1,0,0]

    global cnt
    # if graph[y][x] == 0:
    #     graph[y][x] = 1
    #     cnt+= 1   

    
    for i in range(len(switch)):
        if x == switch[i][1]-1 and y == switch[i][0]-1 and graph[switch[i][2]-1][switch[i][3]-1] == 0:
            a = switch[i][3]-1
            b = switch[i][2]-1
            # 불을 아예 안킨 경우 or   불을 켰지만 방문을 안했을때 다시 한번 그지점을 확인해야함
            #if (graph[b][a] == 0) or (graph[b][a] == 1 and visited[b][a] is False):
            if (graph[b][a] == 0):
                graph[b][a] = 1
                cnt+= 1    
                
                for i in range(4):
                    xx = a+posx[i]   
                    yy = b+posy[i]
                    if 0<=xx<N and 0<=yy<N and visited[yy][xx] is True:                                        
                        dq.append([a, b])
                        visited[switch[i][2]-1][switch[i][3]-1] = True
                        for j in range(4):
                            xx = a+posx[j]   
                            yy = b+posy[j]
                            if 0<=xx<N and 0<=yy<N and graph[yy][xx] == 1 and visited[yy][xx] is False:                                        
                                dq.append([xx, yy])
                                visited[yy][xx] = True
                        #break            
    return dq


    
def bfs(x, y):
    dq = deque([])
    dq.append([x, y])    
    graph[y][x] = 1  
    posx = [0,0,1,-1]
    posy = [1,-1,0,0]
    while dq:
        tmpx, tmpy = dq.popleft()
        #visited[tmpy][tmpx] = True    
          
        dq2 = light(tmpx, tmpy)       
        dq = dq+dq2
        for i in range(4):
            xx = tmpx+posx[i]   
            yy = tmpy+posy[i]

            if 0<=xx<N and 0<=yy<N and graph[yy][xx]==1 and visited[yy][xx] is False:   
                dq.append([xx, yy])                             
                visited[yy][xx]= True

bfs(0, 0)
print(cnt)
# for i in graph:
#     print(i)

# for i in visited:
#     print(i)
# cnt = 0
# for y in range(len(graph)):
#     for x in range(len(graph)):
#         if graph[y][x] == 1:
#             cnt += 1
# print(cnt)
