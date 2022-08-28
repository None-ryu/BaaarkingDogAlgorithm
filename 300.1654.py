import sys
input = sys.stdin.readline
K, N = map(int, input().split())
line = []
for _ in range(K):
    line.append(int(input()))
line.sort()
st = 1
ed = line[-1]
answer = 1
while st <= ed:
    mid = (st+ed)//2
    cnt = 0
    for i in line:
        cnt += i//mid
    if cnt >= N:
        st = mid+1
        answer = mid
    else:
        ed = mid-1
print(answer)