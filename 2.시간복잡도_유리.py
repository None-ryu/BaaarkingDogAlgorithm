def func2(arr, N):
    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            if arr[x]+arr[y] == 100:
                print(1)
                return
    print(0)
func2([1, 52, 48], 3)
func2([50, 42], 2)
func2([4, 13, 63, 87], 4)

