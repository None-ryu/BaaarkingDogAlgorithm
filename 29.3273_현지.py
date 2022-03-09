n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
check = [0]*(x+1)
for i in arr:
    if i > x:
        continue
    else:
        if check[x-i] != 0:
            cnt += 1
        check[i] = 1
print(cnt)