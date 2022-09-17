# https://www.acmicpc.net/problem/3151
import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))
#print(arr)
answer = 0
def binary_serach(num1, left):
    global answer    
    right = N-1
    check = N-1
    while left < right:
        if -1*num1 == arr[left]+arr[right]:
            if arr[left] == arr[right]:
                answer += (right-left)
            #print(num1, arr[left], arr[right])
            else:                                
                #오른쪽 체크
                if check > right:# 새로 새는 경우
                    check = right                
                while check>0 and arr[check] == arr[right]:                    
                    check -= 1   
                                     
                answer += (right-check)
            left += 1
        else:   
            if arr[left]+arr[right] <= -1*num1:
                left = left + 1
            else:
                right = right - 1

for num in range(N-2):
    num1 = arr[num]
    binary_serach(num1, num+1)
print(answer)