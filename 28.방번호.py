# https://www.acmicpc.net/problem/1475
import math 
arr = [0]*9 #9 제외 0~8
nList = list(map(int, input()))

for i in nList:
    if i == 9:
        i = 6
    arr[i]+=1

arr[6] = math.ceil(arr[6]/2)
print(max(arr))