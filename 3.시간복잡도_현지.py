def func3(N):
    for i in range(1, N):
        if i**2 > N:
            print(0)
            return
        if i**2 == N:
            print(1)
            return
    print(0)
func3(9)
func3(693953651)
func3(756580036)