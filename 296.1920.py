N = int(input())
Alist = sorted(list(map(int, input().split())))
M = int(input())
Mlist = list(map(int, input().split()))
def find(number, st, ed):
    if Alist[st] == number or Alist[ed] == number:
        print(1)
        return
    elif st > ed or st == ed:
        print(0)
        return
    else:
        if Alist[(st+ed)//2] > number:
            find(number, st, (st+ed)//2-1)
        elif Alist[(st+ed)//2] == number:
            print(1)
            return
        elif Alist[(st+ed)//2] < number:
            find(number, (st+ed)//2+1, ed)
for i in Mlist:
    find(i, 0, N-1)