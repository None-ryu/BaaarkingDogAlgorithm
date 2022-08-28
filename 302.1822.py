import sys
input = sys.stdin.readline
An, Bn = map(int, input().split())
Alist = sorted(list(map(int, input().split())))
Blist = sorted(list(map(int, input().split())))
answer = []
def find(num):
    st = 0
    ed = Bn-1
    flag = False
    while st <= ed:
        mid = (st+ed)//2
        if Blist[mid] < num:
            st = mid+1
        elif Blist[mid] == num:
            flag = True
            break
        elif Blist[mid] > num:
            ed = mid-1
    if flag == False:
        answer.append(num)
for i in Alist:
    find(i)
try:
    print(len(answer))
    print(*answer)
except:
    print(0)