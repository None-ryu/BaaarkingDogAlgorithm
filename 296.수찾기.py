N = int(input())
numList = list(map(int, input().split()))
numList.sort()
M = int(input())
targetList = list(map(int, input().split()))

def binary_search(target):
    global numList
    global N
    left = 0
    right = N-1    
    while left <= right:
        mid = (left+right) // 2
        if numList[mid] == target:
            return 1
        if numList[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return 0

for i in targetList:
    print(binary_search(i))