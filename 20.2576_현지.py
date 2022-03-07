INF = int(1e9)
total = 0
minimum = INF
for _ in range(7):
    a = int(input())
    if a%2 != 0:
        total += a
        minimum = min(minimum, a)
if total == 0:
    print(-1)
else:
    print(total)
    print(minimum)