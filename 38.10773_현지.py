K = int(input())
money = []
for _ in range(K):
    k = int(input())
    if k != 0:
        money.append(k)
    else:
        money.pop()
print(sum(money))