# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# B = []
# for i in range(N):
#     if A[i] < X:
#         B.append(A[i])
# print(*B)

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i > X:
        A.pop(i) # pop은 번호로 호출해서 불가능
print(*A)