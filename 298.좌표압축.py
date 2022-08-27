# https://www.acmicpc.net/problem/18870
import sys
N = int(input())
numList = list(map(int, sys.stdin.readline().split()))
sortList = set(numList)
sortList = sorted(list(sortList))

def lower_bound(target):
    global sortList
    left = 0
    right = len(sortList)-1

    while left <= right:
        mid = (left+right) // 2
        if sortList[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

for i in numList:
     print(lower_bound(i), end=" ")