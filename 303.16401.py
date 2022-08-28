import sys
input = sys.stdin.readline
M, N = map(int, input().split())
snack = sorted(list(map(int, input().split())))
st = 1
ed = snack[-1]
answer = 0
while st <= ed:
    mid = (st+ed)//2
    cnt = 0
    for i in snack:
        cnt += i//mid
    if cnt >= M:
        st = mid+1
        answer = max(mid, answer)
    else:
        ed = mid-1
print(answer)