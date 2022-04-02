# https://www.acmicpc.net/problem/10866
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queuelist = deque([])

result = []
for i in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push_front':
        queuelist.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        queuelist.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(queuelist) != 0:
            result.append(queuelist.popleft())
        else:
            result.append(-1)
    elif cmd[0] == 'pop_back':
        if len(queuelist) != 0:
            result.append(queuelist.pop())
        else:
            result.append(-1)
    elif cmd[0] == 'size':
        result.append(len(queuelist))
    elif cmd[0] == 'front':
        if len(queuelist) == 0:
            result.append(-1)
        else:
            result.append(int(queuelist[0]))
    elif cmd[0] == 'back':
        if len(queuelist) == 0:
            result.append(-1)
        else:
            result.append(int(queuelist[len(queuelist)-1]))
    elif cmd[0] == 'empty':
        if len(queuelist) == 0:
            result.append(1)
        else:
            result.append(0)
for i in result:
    print(i)