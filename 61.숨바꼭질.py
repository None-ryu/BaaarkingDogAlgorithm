# https://www.acmicpc.net/problem/1697
from collections import deque
N, K = map(int, input().split())
def bfs():
    visited = [False]*100001
    dq = deque([])
    dq.append([N, 0])

    while dq:
        num, cnt = dq.popleft()
        if num == K:
            print(cnt)
            break
        for k in [1, -1, 2]:
            if k == 2:
                tmp = num*2
            else:
                tmp = num+k
            if 0 <= tmp <= 100000:                
                if visited[tmp] is False:
                    dq.append([tmp, cnt+1])
                    visited[tmp] = True
bfs()

# 메모리 초과  : 
# 좌표의 상한을 정해놓지 않으면 최악의 경우 
# 큐에 엄청나게 많은 원소가 들어가게 됩니다.
# https://www.acmicpc.net/board/view/73569

# 방문처리가 필요하다 (쓸모없는 탐색을 줄이기 위해)
# 3에서 시작해서 
# 1) 이동한경우 +1+1+1 => 6 
# 2) 순간이동한 경우 3*2=6
# 2)번인 순간이동한 경우 먼저 도달하게 되고 이때부터 1번은 완전 제외된다 무슨짓을 하더라도 2번보다 많은 시간이 걸리기 때문
# 즉 1번은 더이상 탐색할 필요가 없다 2번에서 6을 방문처리하면 1번은 더이상 탐색하지 않게됨

# 좌표가 0<=N<=100000 사이이기 때문에 visited는 0포함해서 100001개 필요
# visited = [False]*100001