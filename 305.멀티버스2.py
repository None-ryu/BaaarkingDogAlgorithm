# https://www.acmicpc.net/problem/2805
import sys
input = sys.stdin.readline
M, N= map(int, input().split()) # M우주 N행성
spaceArr = []

def getDict(arr): # 1 2 3 2 4
    ziparr = sorted(list(set(arr))) # 1 2 3 4
    arrDict = {}
    for i in range(len(ziparr)): # 값:등수
        arrDict[ziparr[i]] = i #[(1, 0), (2, 1), (3, 2), (4, 3)]
    
    for i in range(len(arr)):
        arr[i] = arrDict[arr[i]]
    return arr

for i in range(M):
    arr = list(map(int, input().split()))
    spaceArr.append(getDict(arr))

answer = 0
for i in range(M):
    for j in range(i+1, M):         
        if spaceArr[i] == spaceArr[j]:
            answer += 1
print(answer)