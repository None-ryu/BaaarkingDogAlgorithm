# https://www.acmicpc.net/problem/13300
import math
N, K = map(int, input().split())
girls = [0] * 7
boys = [0] * 7
for i in range(N):
    sex, grade = map(int, input().split())
    if sex == 0: # 여자
        girls[grade] += 1
    else:
        boys[grade] += 1

cnt = 0
for i in girls:
    if i == 0:
        continue
    cnt += math.ceil(i / K)
for i in boys:
    if i == 0:
        continue
    cnt += math.ceil(i / K)
print(cnt)