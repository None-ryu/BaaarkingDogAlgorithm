def func1(N):
    sum = 0
    for i in range(1, N+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
func1(16)
func1(34567)
func1(27639)