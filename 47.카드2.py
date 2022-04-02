# https://www.acmicpc.net/problem/2164
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
cardlist = deque([i+1 for i in range(N)]) # 1 2 3 4
for i in range(N-1):
    cardlist.popleft()
    cardlist.append(cardlist.popleft())
print(cardlist[0])
