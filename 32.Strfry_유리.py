# https://www.acmicpc.net/problem/11328
N = int(input())
for i in range(N):
    A, B = input().split()
    A = sorted(A)
    B = sorted(B)
    if A==B:
        print('Possible')
    else:
        print('Impossible')