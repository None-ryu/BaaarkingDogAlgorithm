def func3(N):
    for i in range(N):
        if i*i > N:
            print(0)
            return
        if i * i == N:
            print(1)
            return
    print(0)
func3(9)
func3(693953651)
func3(756580036)