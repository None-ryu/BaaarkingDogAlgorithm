import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree = sorted(list(map(int, input().split())))
low = 0
high = tree[-1]-1
while low <= high:
    mid = (low+high)//2
    cnt = 0
    for i in tree:
        if i-mid >= 0:
            cnt += i-mid
    if cnt < M:
        high = mid-1
    elif cnt >= M:
        low = mid+1
print(high)