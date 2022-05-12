# https://www.acmicpc.net/problem/1600
# python3 시간초과 발생
from collections import deque
import sys

K = int(input())
W, H = map(int, input().split())
graph = []
for i in range(H):
    tmplist = list(map(int, input().split()))    
    graph.append(tmplist)

visited = [[ [False]*(K+1) for _ in range(W)] for _ in range(H)]

dq = deque([])
dq.append([0, 0, 0, 0])
visited[0][0][0] = True

# 0~3원숭이 4~11 말
posX = [0,0,1,-1,        -1, 1, -2, 2,  -2, 2, -1, 1]
posY = [1,-1,0,0,         2, 2, 1, 1,   -1, -1, -2, -2]

while dq:
    x, y, kcnt, result = dq.popleft()

    if x==W-1 and y==H-1:
        print(result)
        sys.exit()
    for i in range(12):
        tmpx = x+posX[i]
        tmpy = y+posY[i]
        
        if 0<=tmpx<W and 0<=tmpy<H:                        
                # 장애물 자리에는 못 감
                if graph[tmpy][tmpx] == 1:
                    continue                   

                # 원숭이의 이동은 kcnt가 유지된 상태   
                if i<4 and visited[tmpy][tmpx][kcnt] is False:
                    dq.append([tmpx, tmpy, kcnt, result+1])
                    visited[tmpy][tmpx][kcnt] = True 
                elif i>=4:
                    # 말읭 이동은 kcnt가 증가된 값을 탐색
                    if kcnt < K and visited[tmpy][tmpx][kcnt+1] is False:
                        dq.append([tmpx, tmpy, kcnt+1, result+1])
                        visited[tmpy][tmpx][kcnt+1] = True 
print(-1)
"""
k = 2 일때 visited
[
[[10, 10], [10, 10], [10, 10], [10, 10], [10, 10]], 
[[10, 10], [10, 10], [10, 10], [10, 10], [10, 10]]
]



시간초과 안나오는 다른 사람 코드
# https://www.acmicpc.net/problem/1600

from collections import deque
import sys

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]

dq = deque([])
dq.append([0, 0, 0, 0])
visited[0][0][0] = True

# 0~3원숭이 4~11 말
#posX = [0,0,1,-1,        -1, 1, -2, 2,  -2, 2, -1, 1]
#posY = [1,-1,0,0,         2, 2, 1, 1,   -1, -1, -2, 2]

while dq:
    x, y, kcnt, result = dq.popleft()

    if x==W-1 and y==H-1:
        print(result)
        sys.exit()
    for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
        tmpx = x+di
        tmpy = y+dj    
        if 0<=tmpx<W and 0<=tmpy<H and visited[tmpy][tmpx][kcnt] is False and graph[tmpy][tmpx] == 0:                                    
            # 원숭이의 이동은 kcnt가 유지된 상태   
            dq.append([tmpx, tmpy, kcnt, result+1])
            visited[tmpy][tmpx][kcnt] = True 

    if kcnt<K:
        for di, dj in ((1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1),(-2,-1)):        
            tmpx = x+di
            tmpy = y+dj
            # 말읭 이동은 kcnt가 증가된 값을 탐색
            if  0<=tmpx<W and 0<=tmpy<H and visited[tmpy][tmpx][kcnt+1] is False and graph[tmpy][tmpx] == 0:
                dq.append([tmpx, tmpy, kcnt+1, result+1])
                visited[tmpy][tmpx][kcnt+1] = True 
print(-1)
"""


