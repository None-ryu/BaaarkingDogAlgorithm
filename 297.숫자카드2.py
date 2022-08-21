# https://www.acmicpc.net/problem/10816
import sys
N = int(input())
numList = list(map(int, sys.stdin.readline().split()))
numList.sort()
M = int(input())
targetList = list(map(int, sys.stdin.readline().split()))

def binary_search(target):
    global numList
    global N
    left = 0
    right = N-1    
    while left <= right:
        mid = (left+right) // 2
        if numList[mid] == target:
            print("mid", mid)
            return 1
        if numList[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return 0

def lower_bound2(target):
    global numList
    global N
    left = 0
    right = N-1   
    while left <= right:
        mid = (left+right) // 2  
        if numList[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

#-----------------------------------
def upper_bound2(target):
    global numList
    global N
    left = 0
    right = N-1   
    while left <= right:
        mid = (left+right) // 2  
        if numList[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

def lower_bound(target):
    global numList
    global N
    left = 0
    right = N   
    while left < right:
        mid = (left+right) // 2  
        if numList[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def upper_bound(target): # 실패
    global numList
    global N
    left = 0
    right = N   
    while left < right:
        mid = (left+right) // 2  
        if numList[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return right

# 5
# 1 2 2 2 3
# 1
# 2

for target in targetList:
    #print(binary_search(i))
    #print(upper_bound2(target))
    #print(upper_bound(target))
    L = lower_bound2(target) #1
    R = upper_bound2(target) #3
    print(R-L+1, end=" ")

    # result = lower_bound(target)
    # cnt = 0
    # for num in range(result, N):
    #     if numList[num] == target:
    #         cnt += 1
    #     else:
    #         break
    # print(cnt, end=" ")