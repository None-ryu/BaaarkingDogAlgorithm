from collections import deque
import sys
import copy
input = sys.stdin.readline
N, M = map(int, input().split())
queue = deque([])
total = 0
for i in range(1, N+1):
    queue.append(i)
abc = list(map(int, input().split()))
for i in range(M):
    leftcnt = 0
    rightcnt = 0
    if abc[i] != queue[0]:
        leftqueue = copy.deepcopy(queue)
        rightqueue = copy.deepcopy(queue)
        while True:
            leftqueue.rotate(1)
            leftcnt += 1
            if abc[i] == leftqueue[0]:
                break
        while True:
            rightqueue.rotate(-1)
            rightcnt += 1
            if abc[i] == rightqueue[0]:
                break
        mincnt = min(leftcnt, rightcnt)
        total += mincnt
        if mincnt == leftcnt:
            for _ in range(mincnt):
                queue.rotate(1)
        else:
            for _ in range(mincnt):
                queue.rotate(-1)
        queue.popleft()
    else:
        queue.popleft()
print(total)