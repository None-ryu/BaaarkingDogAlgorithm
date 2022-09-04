# https://www.acmicpc.net/problem/2467
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N-1

rleft = 0
rright = N-1
result = abs((arr[left] + arr[right]))

# left <= right라면 left랑 right가 같은 값을 가리키는 경우 오답
while left<right:    
    if abs((arr[left] + arr[right])) <= result:
            result = abs((arr[left] + arr[right]))  
            rleft = left
            rright = right

    # mid값으로 비교하는것이 아니기 때문에 
    # left나 right값을 변동하면서 하나씩 본다
    if arr[left] + arr[right] < 0:                
        left = left + 1 
    else:
        right = right - 1

print(arr[rleft], arr[rright])


"""
left <= right 오답 케이스 

input:
4
-3 -2 -1 2

answer:
-2 2
"""