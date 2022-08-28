# # pypy로만 통과
# import sys
# input = sys.stdin.readline
# M, N = map(int, input().split())
# snack = sorted(list(map(int, input().split())))
# st = 1
# ed = snack[-1]
# answer = 0
# while st <= ed:
#     mid = (st+ed)//2
#     cnt = 0
#     for i in snack:
#         cnt += i//mid
#     if cnt >= M:
#         st = mid+1
#         answer = max(mid, answer)
#     else:
#         ed = mid-1
# print(answer)

# python3로도 통과
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
snack = list(map(int, input().split()))
snack.sort()
st = 1
ed = snack[-1]

def line(mid): 
    #print(mid)   
    cnt = 0
    for num in snack:
        cnt += (num // mid)
    return cnt

while st <= ed:
    mid = (st+ed)//2
    cnt = line(mid)
    if cnt >= M:
        st = mid+1
    else:
        ed = mid-1
print(ed)