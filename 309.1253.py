import sys
input = sys.stdin.readline
N = int(input())
Alist = sorted(list(map(int, input().split())))
answer = 0
for i in range(len(Alist)):
    st = 0
    ed = N-2
    tmp = Alist[0:i] + Alist[i+1:N]
    while st < ed:
        if tmp[st] + tmp[ed] < Alist[i]:
            st += 1
        elif tmp[st] + tmp[ed] > Alist[i]:
            ed -= 1
        elif tmp[st] + tmp[ed] == Alist[i]:
            answer += 1
            break
print(answer)