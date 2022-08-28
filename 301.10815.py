import sys
input = sys.stdin.readline
N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
check = list(map(int, input().split()))
answer = []
def find(num):
    flag = False
    st = 0
    ed = N-1
    while st <= ed:
        mid = (st+ed)//2
        if card[mid] < num:
            st = mid+1
        elif card[mid] == num:
            answer.append(1)
            flag = True
            break
        elif card[mid] > num:
            ed = mid-1
    if flag == False:
        answer.append(0)
for i in check:
    find(i)
print(*answer)