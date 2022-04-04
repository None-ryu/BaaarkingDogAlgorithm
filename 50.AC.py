# https://www.acmicpc.net/problem/5430
from collections import deque
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    stat = 'F'
    ck = True
    p = list(input().strip())
    n = int(input())
    tmp = list(input().strip().split(','))
    #print(p, n, tmp)
    queue = deque()

    if tmp[0] != "[]":
        for i in range(len(tmp)):
            tmpv = tmp[i]
            tmpv = tmpv.replace("[", "")
            tmpv = tmpv.replace("]", "")
            queue.append(int(tmpv))
        
    for cmd in p:
        if cmd == 'R':
            if stat == 'F':
                stat = 'R'
            elif stat == 'R':
                stat = 'F'
        else:
            if len(queue)==0:
                print("error")
                ck= False
                break
            if stat == 'F':
                queue.popleft()
            else:
                queue.pop()
        #print(cmd, queue)
    if ck is True:
        if stat == 'R':
            queue.reverse()
        print("[", end="")
        for q in range(len(queue)):
            if q == len(queue)-1:
                print(queue[q], end="")

            else:
                print(queue[q], end=",")
        print("]\n", end="")