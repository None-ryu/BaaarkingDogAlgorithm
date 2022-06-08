from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001

dq = deque([])
dq.append([N, 0])
visited[N] = True
pos = [2, 1, -1] # 2를 먼저 탐색하지 않으면 N=1, K=2 인 경우 0이 아닌 1이 나옴, visited때문에 *2는 append를 안함
while dq:
    num, cnt = dq.popleft()
    if num == K:
        print(cnt)
        break
    for i in range(3):
        tmp = num+pos[i]
        if pos[i] == 2:
            tmp = num*2

        if 0<=tmp and tmp<=100000 and visited[tmp] is False:
            if pos[i] == 2:            
                dq.appendleft([tmp, cnt]) # 두배로 처리한 애를 먼저봐야 최소 cnt로 도달할 수 있음
            else:            
                dq.append([tmp, cnt+1])
            visited[tmp] = True
        