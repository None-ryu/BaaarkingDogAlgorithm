# https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
#print(arr)

def line(mid):
    print(mid)
    if mid == 0:
        return 0
    global K
    cnt = 0
    for num in arr:
        cnt += (num // mid)
    if num == K:
        return cnt
    else:
        return cnt

ans = 0
def upper_bound():
    global K
    global arr
    left = 1
    right = arr[-1]

    while left <= right:
        mid = (left + right) // 2

        if line(mid) >= K:
            left = mid + 1
        else:
            right = mid - 1
    print(left, right, mid)
    return right      

print(upper_bound())