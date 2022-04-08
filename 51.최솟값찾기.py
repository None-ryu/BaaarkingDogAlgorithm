# https://www.acmicpc.net/problem/11003
from collections import deque
import sys
input = sys.stdin.readline


N, L = map(int, input().split()) # 12 5
Dlist = list(map(int, input().split())) # 0~11

dq = deque()
#result = []
for i in range(N):
    while dq and dq[-1][0] > Dlist[i]:
        dq.pop()

    while dq and dq[0][1] < i-L+1: 
        dq.popleft()        
    dq.append((Dlist[i], i)) # 
    #print(i, Dlist[i], dq)
    #result.append(dq[0][0])
    print(dq[0][0], end=" ")



