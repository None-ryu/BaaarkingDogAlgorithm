# https://www.acmicpc.net/problem/1822
import sys
input = sys.stdin.readline

N, M= map(int, input().split())
narr = list(map(int, input().split()))
narr.sort()
marr = list(map(int, input().split()))
marr.sort()

totalarr = list(set(narr+marr))
totalarr.sort()
#print(totalarr)

def binary_search(arr, target):        
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    #print(left, right, mid)
    return False      

ans = []
for i in totalarr:
    if binary_search(narr, i) is True:
        if binary_search(marr, i) is False:
            ans.append(i)

print(len(ans))
if len(ans) > 0:
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