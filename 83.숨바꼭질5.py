# https://www.acmicpc.net/problem/17071
from collections import deque
import sys
N, K = map(int, input().split())
visited = [[-1] * 500001 for _ in range(2)]

dq = deque([])
dq.append([N, 0, 0, K])
visited[0][N] = 0

pos = [2, 1, -1] # 2를 먼저 탐색하지 않으면 N=1, K=2 인 경우 0이 아닌 1이 나옴, visited때문에 *2는 append를 안함
#pos = [1, -1]

if N == K:
    print(0)
    sys.exit()
while dq:
    num, cnt, kcnt, tmpK = dq.popleft() # 5 0 0 17
    
    if tmpK > 500000:
        print(-1)
        break
    
    kcnt = kcnt+1
    tmpK = kcnt+tmpK  
    for i in range(len(pos)):
        tmp = num+pos[i]                              
        #tmparr= arr
        if pos[i] == 2:
            tmp = num*2
        
        if 0<=tmp and tmp<= 500000:                
            if visited[(cnt+1)%2][tmp] == -1: 
                dq.append([tmp, cnt+1, kcnt, tmpK])
            visited[(cnt+1)%2][tmp] = cnt+1

young = K
time = 0
for i in range(0, 500000):
    young+= i

    if young > 500000:
        print(-1)
        sys.exit()
    if visited[i%2][young]!=-1 and visited[i%2][young]<=i:
        print(i)
        sys.exit()
print(-1)


        
        