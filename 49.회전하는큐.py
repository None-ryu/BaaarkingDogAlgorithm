# https://www.acmicpc.net/problem/1021
from collections import deque
import sys
input = sys.stdin.readline
N, M  = map(int, input().split())
Nlist = deque([i+1 for i in range(N)])
removelist = list(map(int, list(input().split())))

def getLeft(num):
    leftcnt = 0
    for i in Nlist:
        if i != num:
            leftcnt+=1
        else:
            return leftcnt

result = 0
for i in removelist:
    if i == Nlist[0]:
        Nlist.popleft()
    else:
        leftcnt = getLeft(i)
        if leftcnt < len(Nlist)-leftcnt:
            result+=leftcnt
            for lc in range(leftcnt):
                Nlist.rotate(-1)
        else:
            result+=len(Nlist)-leftcnt
            for lc in range(len(Nlist)-leftcnt):
                Nlist.rotate(1)
        Nlist.popleft()
print(result)