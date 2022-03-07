table = []
for _ in range(5):
    table.append(int(input()))
table.sort()
print(sum(table)//5)
print(table[2])