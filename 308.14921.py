import sys
input = sys.stdin.readline
N = int(input())
solution = list(map(int, input().split()))
result = 2147483647
if N == 2:
    print(sum(solution))
    sys.exit()
for i in range(N):
    if solution[i] < 0:
        low = i+1
        high = N-1
    else:
        low = 0
        high = i-1
    mid = (low+high)//2
    while low <= high:
        mid = (low+high)//2
        if solution[i] + solution[mid] > 0:
            high = mid-1
        elif solution[i] + solution[mid] == 0:
            print(0)
            sys.exit()
        elif solution[i] + solution[mid] < 0:
            low = mid+1
        if abs(solution[i]+solution[mid]) <= abs(result):
            result = solution[i]+solution[mid]
print(result)