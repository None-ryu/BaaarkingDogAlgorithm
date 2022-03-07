# https://www.acmicpc.net/problem/10093

AA, BB = map(int, input().split())
# AA가 BB보다 클 경우
A = min(AA, BB)
B = max(BB, AA)
if A == B: # A와 B가 동일한 경우 
    print(0)
else:
    print(B-A-1)
    for i in range(1, B-A):
        print(i+A, end=" ")