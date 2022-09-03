# https://www.acmicpc.net/problem/2805
import sys
input = sys.stdin.readline

N, M= map(int, input().split())
arr = list(map(int, input().split()))

def line(mid): 
    #print(mid)   
    total = 0
    for num in arr:
        if num-mid > 0:
            total += (num-mid)
    return total

def upper_bound():
    global M
    left = 1
    right = max(arr)   
    while left <= right:
        mid = (left + right) // 2
        linecnt = line(mid)
        if linecnt >= M:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(upper_bound())

