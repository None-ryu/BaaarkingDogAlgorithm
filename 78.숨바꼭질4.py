# https://www.acmicpc.net/problem/13913
from collections import deque
import copy

N, K = map(int, input().split())
visited = [False] * 100001

dq = deque([])
dq.append([N, 0, str(N)])
visited[N] = True
pos = [2, 1, -1] # 2를 먼저 탐색하지 않으면 N=1, K=2 인 경우 0이 아닌 1이 나옴, visited때문에 *2는 append를 안함
while dq:
    num, cnt, arr = dq.popleft()
    if num == K:
        print(cnt)
        tmplist = list(map(int, arr.split(",")))
        print(*tmplist)
        break
    for i in range(3):
        tmp = num+pos[i]
        tmparr= arr
        if pos[i] == 2:
            tmp = num*2

        if 0<=tmp and tmp<=100000 and visited[tmp] is False:        
            tmparr += (","+str(tmp))
            dq.append([tmp, cnt+1, tmparr])
            visited[tmp] = True
            
        