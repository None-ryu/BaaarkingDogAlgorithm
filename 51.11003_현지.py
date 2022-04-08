from collections import deque
import sys
input = sys.stdin.readline
N, L = map(int, input().split())
A = list(map(int, input().split()))
arr = deque()
for i in range(N):
    while arr and arr[-1][0] > A[i]:
        arr.pop()
    while arr and arr[0][1] < i-L+1:
        arr.popleft()
    arr.append((A[i], i))
    print(arr[0][0], end=" ")