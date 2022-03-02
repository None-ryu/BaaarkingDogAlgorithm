N, X = map(int, input().split())
arr = list(map(int, input().split()))
result = []
for i in arr:
    if i < X:
        result.append(i)
print(*result)