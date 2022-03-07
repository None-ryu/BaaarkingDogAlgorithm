st, ed = map(int, input().split())
if ed > st:
    if ed-st == 1:
        print(0)
    else:
        print(ed-st-1)
        for i in range(1, ed-st):
            print(st+i, end=" ")
if st > ed:
    if st-ed == 1:
        print(0)
    else:
        print(st-ed-1)
        for i in range(1, st-ed):
            print(ed+i, end=" ")
if st == ed:
    print(0)