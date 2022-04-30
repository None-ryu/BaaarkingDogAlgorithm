# https://www.acmicpc.net/problem/2206
from collections import deque
import sys 
N, M = map(int, input().split()) #N y
graph = []
visited = [ [[-1]*2 for _ in range(M)] for _ in range(N)]
# -1 (벽 부순것) :  지금까지 벽을 한번이라도 부순 경우
# [-1 ( 일반), -1 (벽 부순것)]    
# [
# [[-1, -1], [-1, -1], [-1, -1], [-1, -1]], 
# [[-1, -1], [-1, -1], [-1, -1], [-1, -1]], 
# [[-1, -1], [-1, -1], [-1, -1], [-1, -1]], 
# [[-1, -1], [-1, -1], [-1, -1], [-1, -1]], 
# [[-1, -1], [-1, -1], [-1, -1], [-1, -1]], 
# [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
# ]

# print(visited)
for i in range(N):
    tmp = list(map(int, list(input())))
    graph.append(tmp)


posx = [0,0,1,-1]
posy = [1,-1, 0,0]
dq = deque()
dq.append([0, 0, 'n', 1]) # n은 normal w는 벽부순것
visited[0][0][0] = 1


while dq:
    tmpx, tmpy, wall, cnt = dq.popleft()
    if tmpx == M-1 and tmpy == N-1:
        print(cnt)        
        sys.exit()    
    for i in range(4):
        xx = tmpx + posx[i]
        yy = tmpy + posy[i]

        if 0<=xx<M and 0<=yy<N:
            # 벽을 한번이라도 부순경우
            if wall == 'w':
                if graph[yy][xx] == 0 and visited[yy][xx][1] == -1 and visited[yy][xx][0] == -1 :
                    dq.append([xx, yy, wall, cnt+1]) 
                    visited[yy][xx][1] = cnt+1

                # # 지금만난 영역이 벽인 경우  벽을 부수지 못함
                # if graph[yy][xx] == 1 and visited[yy][xx][0] == -1:
                #     dq.append([xx, yy, wall, cnt+1]) 
                #     visited[yy][xx][0] = cnt+1
                # # 지금만난 영역이 벽이 아닌 경우 벽을 부술필요가 없다
                # elif graph[yy][xx] == 0 and visited[yy][xx][0] == -1:
                #     dq.append([xx, yy, wall, cnt+1]) 
                #     visited[yy][xx][0] = cnt+1
            
            # 벽을 한번도 안 부순 경우
            else:
                # 지금만난 영역이 벽인 경우  
                if graph[yy][xx] == 1:                                        
                    # 새로 만난 벽을 부수는 경우
                    if  visited[yy][xx][1] == -1 and visited[yy][xx][0] == -1:
                        dq.append([xx, yy, 'w', cnt+1]) 
                        visited[yy][xx][1] = cnt+1                        
                
                # 지금 만난 영역이 벽이 아닌 경우
                else:
                    if visited[yy][xx][0] == -1:
                        dq.append([xx, yy, wall, cnt+1]) 
                        visited[yy][xx][0] = cnt+1
print(-1)