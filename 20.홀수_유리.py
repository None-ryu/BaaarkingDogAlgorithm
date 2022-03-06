# https://www.acmicpc.net/problem/2576

total = 0
minNum = 100
for i in range(7):
    N = int(input())
    if N % 2 == 1:
        if minNum > N:
            minNum = N
        total += N
if total != 0:
    print(total)
    print(minNum)
else:
    print(-1)