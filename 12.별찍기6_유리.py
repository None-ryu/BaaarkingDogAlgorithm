
# https://www.acmicpc.net/problem/2442

N = int(input())
for i in range(N):
    print(" "*(i) + "*"*(2*(4-i)+1))


"""
    *   4   1
   *** 3     3
  ***** 2     5
 ******* 1      7
********* 0     9 2xi+1


********* 9 0
 ******* 7   1
  ***** 5   2
   *** 3    3
    * 1     4
"""
