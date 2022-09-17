# https://www.acmicpc.net/problem/14921
import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))

left = 0
right = N-1
min = abs(arr[left] + arr[right])
result = arr[left] + arr[right]
while left < right:
    if abs(arr[left] + arr[right]) < min:
        min = abs(arr[left] + arr[right])
        result = arr[left] + arr[right]
    if arr[left] + arr[right] < 0:
        left += 1
    else:
        right -= 1
print(result)