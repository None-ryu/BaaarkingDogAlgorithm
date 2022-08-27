import sys
input = sys.stdin.readline
N = int(input())
Xlist = list(map(int, input().split()))
Ylist = sorted(list(set(Xlist)))
def find(num):
    st = 0
    ed = len(Ylist)-1
    while True:
        mid = (st+ed)//2
        if Ylist[mid] < Xlist[num]:
            st = mid+1
        elif Ylist[mid] == Xlist[num]:
            Xlist[num] = mid
            break
        elif Ylist[mid] > Xlist[num]:
            ed = mid-1
for i in range(len(Xlist)):
    find(i)
print(*Xlist)