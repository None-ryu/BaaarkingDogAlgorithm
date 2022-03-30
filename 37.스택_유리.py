# https://www.acmicpc.net/problem/10828
from collections import deque
import sys
input =  sys.stdin.readline
N = int(input())

stacklist = deque()
for i in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push':
        stacklist.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stacklist) > 0 :
            print(stacklist.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':  
        print(len(stacklist))
    elif cmd[0] == 'empty':  
        if len(stacklist) == 0 :
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stacklist) == 0 :
            print(-1)
        else:
            print(stacklist[-1])