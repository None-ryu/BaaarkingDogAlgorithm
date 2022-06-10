# https://www.acmicpc.net/problem/2447
import sys
sys.setrecursionlimit(10**6)
'''

 3 = 3^1
*** 0  
* * 1
*** 2

 9 = 3^2
********* 0  3개짜리 3개
* ** ** *
********* 2

***   *** 3  3개짜리 2개
* *   * * 4
***   *** 5

********* 6  3개짜리 3개
* ** ** * 7
********* 8

27 9 3
'''
N = int(input())
graph = [[' ']*N for _ in range(N)]

def recur(size, xx, yy):
    if size == 3:
        cnt = 0
        for y in range(yy, yy+size):
            for x in range(xx, xx+size):    
                cnt += 1
                if cnt != 5:
                    graph[y][x] = '*'
    else:            
        cnt =0
        size = size // 3
        for y in range(3):
            for x in range(3):
                cnt += 1
                if cnt != 5:
                    recur(size, xx+x*size, yy+y*size) # 3 0 0
recur(N, 0, 0)

for tmp in graph:    
    print(*tmp, sep="")
    
