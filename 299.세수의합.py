# https://www.acmicpc.net/problem/2295
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
#print(arr)

tmparr = set()
for a in range(len(arr)):
    for b in range(a, len(arr)):
        tmparr.add(arr[a]+arr[b])
tmparr = sorted(list(tmparr))
#print(tmparr)

def binary_search(target):
    global tmparr
    
    left = 0
    right = len(tmparr)-1

    while left<=right:
        mid = (left+right) // 2
        if tmparr[mid] == target:
            return True
        if tmparr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return False

ans = 0
for tmp in arr:
    for a in arr:
        if binary_search(tmp-a):
            ans = max(ans, tmp)
print(ans)