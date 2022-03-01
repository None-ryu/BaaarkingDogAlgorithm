def func4(N):
    total = 1
    while True:
        if total*2 > N:
            break
        total = total*2
    print(total)
func4(5)
func4(97615282)
func4(1024)