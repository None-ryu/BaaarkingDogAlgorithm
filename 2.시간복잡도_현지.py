def func2(arr, N):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if i != j and arr[i]+arr[j] == 100:
                cnt = 1
    if cnt == 1:
        print(1)
    else:
        print(0)
func2([1, 52, 48], 3)
func2([50, 42], 2)
func2([4, 13, 63, 87], 4)