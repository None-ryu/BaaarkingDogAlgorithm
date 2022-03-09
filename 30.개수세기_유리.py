# https://www.acmicpc.net/problem/10807
N = int(input())
nList = list(map(int, input().split()))
num = int(input())
result = 0
for i in nList:
    if i == num:
        result += 1
print(result)