# https://www.acmicpc.net/problem/3273
N = int(input())
nlist = list(map(int, input().split()))
total = int(input())
result = [0]*total # 0~12

cnt = 0
for i in nlist:
    if total <= i:
        continue
    if result[total-i] == 1:
        cnt+=1
    result[i] = 1
print(cnt)