# https://www.acmicpc.net/problem/10773
from collections import deque
import sys
input =  sys.stdin.readline
N = int(input())

stacklist = deque()
for i in range(N):
    number = int(input())
    if number != 0:
        stacklist.append(number)
    else:
        stacklist.pop()
print(sum(stacklist))
    