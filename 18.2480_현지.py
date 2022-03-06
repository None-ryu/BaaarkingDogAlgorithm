a, b, c = map(int, input().split())
number = []
number.append(a)
number.append(b)
number.append(c)
reward = []
for i in range(3):
    cnt = 0
    for j in range(3):
        if number[i] == number[j]:
            cnt += 1
    if cnt == 2:
        reward.append(1000 + number[i]*100)
    if cnt == 3:
        reward.append(10000 + number[i]*1000)
    else:
        reward.append(max(number)*100)
print(max(reward))