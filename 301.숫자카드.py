# https://www.acmicpc.net/problem/10815
import sys
input = sys.stdin.readline

N= map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

M= map(int, input().split())
arr2 = list(map(int, input().split()))
print(arr, arr2)

def binary_search(target):    
    global arr
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    #print(left, right, mid)
    return 0      

for i in arr2:
    print(binary_search(i), end=" ")