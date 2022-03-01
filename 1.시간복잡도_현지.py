N = int(input())
def func1(N):
    Nlist = []
    for i in range(1, N+1):
        Nlist.append(i)
    total = 0
    for i in Nlist:
        if i%3 == 0 or i%5 == 0:
            total += i
    print(total)
func1(N)