import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
Ulist = []
for _ in range(N):
    Ulist.append(int(input()))
Ulist = sorted(Ulist)
two = []
for i in range(len(Ulist)):
    for j in range(len(Ulist)):
        two.append(Ulist[i]+Ulist[j])
two = list(set(two))
result = -INF
for i in range(len(Ulist)-1, -1, -1):
    if Ulist[i] <= result:
        break
    for j in range(len(two)):
        tmp = Ulist[i]-two[j]
        st = 0
        ed = len(Ulist)-1
        while st <= ed:
            mid = (st+ed)//2
            if Ulist[mid] < tmp:
                st = mid+1
            elif Ulist[mid] == tmp:
                result = max(Ulist[i], result)
                break
            elif Ulist[mid] > tmp:
                ed = mid-1
print(result)