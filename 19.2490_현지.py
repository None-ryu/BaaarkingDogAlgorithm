for _ in range(3):
    table = []
    a, b, c, d = map(int, input().split())
    table.append(a)
    table.append(b)
    table.append(c)
    table.append(d)
    if sum(table) == 3:
        print("A")
    if sum(table) == 2:
        print("B")
    if sum(table) == 1:
        print("C")
    if sum(table) == 0:
        print("D")
    if sum(table) == 4:
        print("E")