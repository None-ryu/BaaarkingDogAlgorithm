# https://www.acmicpc.net/problem/1253
import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))

def binary_search(myarr, target):
    left = 0
    right = len(myarr)-1
        
    while left < right:
        if myarr[left]+myarr[right] == target:            
            return True
        if myarr[left] + myarr[right] < target:
            left += 1
        else:
            right -= 1
    return False    

answer = 0
for num in range(len(arr)):
    selectedArr = arr[0:num] + arr[num+1:]
    if binary_search(selectedArr, arr[num]):
        answer += 1
print(answer)