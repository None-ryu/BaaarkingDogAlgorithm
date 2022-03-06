table = []
for _ in range(9):
    table.append(int(input()))
maximum = 0
number = 0
for i in range(len(table)):
    if table[i] > maximum:
        maximum = table[i]
        number = i+1
print(maximum)
print(number)