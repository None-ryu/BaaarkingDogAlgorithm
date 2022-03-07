# https://www.acmicpc.net/problem/2309

# 9개중 7개를 선택하는 조합 문제
import sys
sys.setrecursionlimit(10000)
arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()

result = []
def dfs(depth, start):
 
    if depth == 7 and sum(result) == 100:
        #print(result)
        for i in result:
            print(i)
        sys.exit()
        
    if depth == 7:
        return
    for i in range(start, len(arr)):    
        result.append(arr[i])
        dfs(depth+1, i+1)
        result.pop()
dfs(0, 0)

