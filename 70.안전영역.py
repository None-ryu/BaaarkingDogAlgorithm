# https://www.acmicpc.net/problem/2468
from collections import deque

S = int(input())
graph = []
minv = 1000
maxv = 0
for i in range(S):
    tmplist = list(map(int, input().split()))
    graph.append(tmplist)
    for tmp in tmplist:
        minv = min(minv, tmp)
        maxv = max(maxv, tmp)
if minv>0:
    minv=minv-1
resultCnt = 0 # 영역갯수 최대인것 찾기
resultHeight = 0 # 높이 저장
for height in range(minv, maxv+1):
    #print("HEight", height)
    # 0안전영역 1물에잠김 2방문완료
    visited = [[0]*S for _ in range(S)]
    
    
    # 물에 잠기는 영역 체크
    for y in range(len(graph)):
        for x in range(len(graph)):
            if graph[y][x] <= height:
                visited[y][x] = 1 # 물에 잠김

    cnt = 0
    for y in range(len(graph)):
        for x in range(len(graph)):
            if visited[y][x] == 0:                                
                dq = deque()
                dq.append([x, y])
                visited[y][x] = 2                
                posx = [0,0,1,-1]
                posy = [1,-1, 0,0]

                while dq:
                    tmpx, tmpy = dq.popleft()
                    for i in range(4):
                        xx = tmpx + posx[i]
                        yy = tmpy + posy[i]

                        if 0<=xx<S and 0<=yy<S and visited[yy][xx]==0:
                            visited[yy][xx] = 2
                            dq.append([xx, yy])
                cnt += 1    
    #print(cnt)
    if resultCnt <= cnt:
        resultCnt = cnt
        resultHeight = height
print(resultCnt)