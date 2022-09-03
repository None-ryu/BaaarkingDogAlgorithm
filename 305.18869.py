import sys
input = sys.stdin.readline
M, N = map(int, input().split())
space = []
def compare(uni):
    tmpuni = list(set(uni))
    tmpuni = sorted(uni)
    result = []    
    for i in uni:
        low = 0
        high = N-1
        while low <= high:
            mid = (low+high)//2
            if tmpuni[mid] < i:
                low = mid+1
            elif tmpuni[mid] == i:
                result.append(mid)
                break
            elif tmpuni[mid] > i:
                high = mid-1
    return result
for _ in range(M):
    space.append(compare(list(map(int, input().split()))))
cnt = 0
for i in range(M):
    for j in range(i+1, M):
        if space[i] == space[j]:
            cnt += 1
print(cnt)