A = int(input())
B = int(input())
C = int(input())
for i in range(0, 10):
    cnt = 0
    for j in str(A*B*C):
        if str(i) == j:
            cnt += 1
    print(cnt)