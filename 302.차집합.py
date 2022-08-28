# https://www.acmicpc.net/problem/1822
import sys
input = sys.stdin.readline

N, M= map(int, input().split())
narr = list(map(int, input().split()))
narr.sort()
marr = list(map(int, input().split()))
marr.sort()
#print(totalarr)

def binary_search(target):        
    global marr
    left = 0
    right = len(marr)-1

    while left <= right:
        mid = (left + right) // 2

        if marr[mid] == target:
            return True
        if marr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    #print(left, right, mid)
    return False      

ans = []
for i in narr:
    if binary_search(i) is False:
        ans.append(i)

print(len(ans))
print(*ans)


"""
n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a-b))

c = list(a-b)
c.sort()
for i in c:
    print(i,end=' ')

"""