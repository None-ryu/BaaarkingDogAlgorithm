# https://www.acmicpc.net/problem/16933
from collections import deque
import sys
input = sys.stdin.readline
#INF = int(10**9)
INF = int(10)
N, M, K = map(int, input().split())
graph = []
for i in range(N):
    tmp = list(map(int, input().strip()))
    graph.append(tmp)

visited = [[[INF]*(K+1) for _ in range(M)] for _ in range(N)]
print(visited)


dq = deque([])
dq.append([0,0,0,1,0])
visited[0][0][0] = 1

posx = [0,0,1,-1]
posy = [1,-1,0,0]

while dq:
    x,y,wall,result, day = dq.popleft() # day 짝수는 낮, 밤 홀수
    if(visited[x][y][wall]!=result) :
        continue
    if x==M-1 and y==N-1:
        print(result)
        sys.exit()
    for i in range(4):
        tmpx = x+posx[i]
        tmpy = y+posy[i]
            
        if tmpx<0 or tmpx>=M or tmpy<0 or tmpy>=N:
            continue

        #벽을 부술 수 없는 경우
        if wall >= K and graph[tmpy][tmpx]==0:        
            if visited[tmpy][tmpx][wall][(day+1)%2] is False:
                visited[tmpy][tmpx][wall][(day+1)%2] = True
                dq.append([tmpx,tmpy,wall, result+1, (day+1)%2])

        #벽을 부술 수 있는 경우
        elif wall<K:            
            # 벽인 경우            
            if graph[tmpy][tmpx]==1:
                # 낮인 경우 벽을 부수고 지나간다
                if day%2==0:
                    walltmp = wall+1
                    if visited[tmpy][tmpx][walltmp][(day+1)%2] is False:
                        visited[tmpy][tmpx][walltmp][(day+1)%2] = True
                        dq.append([tmpx,tmpy,walltmp, result+1, (day+1)%2])
                # 밤인 경우 벽을 부수지는 못하지만 거리만 증가
                else:
                    walltmp = wall
                    if visited[tmpy][tmpx][walltmp][(day+1)%2] is False:
                        visited[tmpy][tmpx][walltmp][(day+1)%2] = True
                        dq.append([x,y,walltmp, result+1, (day+1)%2]) # 이동을 안함!!!!
            # 벽이 아닌 경우 낮이고 밤이고 상관이 없음
            else:
                walltmp = wall
                if visited[tmpy][tmpx][walltmp][(day+1)%2] is False:
                    visited[tmpy][tmpx][walltmp][(day+1)%2] = True
                    dq.append([tmpx,tmpy,walltmp, result+1, (day+1)%2])
print(-1)



"""
1 4 1
0010
[[[10, 10], [10, 10], [10, 10], [10, 10]]]


visited에 이동횟수를 저장하고 이동횟수로 짝수인지 홀수인지 판단해서 day를 판단
두번이상 머무를 필요가 없다 
머무르는거를 한번만 해야되는데 몇번 머무르는지 체크를 안하기 때문에 여러번하게됨 
"""