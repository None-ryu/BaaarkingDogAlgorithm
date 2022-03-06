# https://www.acmicpc.net/problem/2480
from collections import defaultdict

mydict = defaultdict(int)
num = list(map(int, input().split()))
cnt = 0
maxnum = 0
for i in range(3):
    mydict[num[i]]+=1
    if cnt<mydict[num[i]]:
        cnt = mydict[num[i]]
        maxnum = num[i]
result = 0
if cnt == 3:
    result = 10000+ maxnum*1000
elif cnt == 2:
    result = 1000+ maxnum*100
else:
    maxnum = max(num)
    result = maxnum * 100
print(result)