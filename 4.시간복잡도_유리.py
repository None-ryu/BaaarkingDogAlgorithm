def func4(N):
    total = 1
    for i in range(N):
        if total * 2 <= N:
            total *= 2
        else:
            print(total)
            return
func4(5)
func4(97615282)
func4(1024)