# https://www.acmicpc.net/problem/2448
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
graph = [[' ']*(N*2-1) for _ in range(N)]

def recur(xx, yy, size):
    if size == 3:
        # 삼각형 별을 채운다
        graph[yy][xx] = '*' # 5, 0
        graph[yy+1][xx-1] = '*' # 4, 1
        graph[yy+1][xx+1] = '*' # 6, 1
        for i in range(5): # (3,2)~(7,2)
            graph[yy+2][xx-2+i] = '*'
    else:                    
        size = size // 2
        recur(xx, yy, size)
        recur(xx-size, yy+size, size)
        recur(xx+size, yy+size, size)
        
recur(N-1, 0, N)

for tmp in graph:    
    print(*tmp, sep="")
    
