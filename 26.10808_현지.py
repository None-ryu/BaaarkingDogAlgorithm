S = list(input())
result = [0]*26
for i in range(97, 123):
    for j in S:
        if j == chr(i):
            result[i-97] += 1
print(*result)