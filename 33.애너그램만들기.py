#https://www.acmicpc.net/problem/1919
from collections import defaultdict
A = input()
B = input()
Adict = defaultdict(int)
Bdict = defaultdict(int)

for i in A:
    Adict[i] += 1

for i in B:
    Bdict[i] += 1

cnt = 0
for k, v in Adict.items():
    cnt += abs(Bdict[k] - v)
    Bdict[k] = 0
    Adict[k] = 0
for k, v in Bdict.items():
    cnt += abs(Adict[k] - v)
    Bdict[k] = 0
    Adict[k] = 0
print(cnt)