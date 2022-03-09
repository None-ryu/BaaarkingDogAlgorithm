# def func2(arr, N):
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if i != j and arr[i]+arr[j] == 100:
#                 cnt = 1
#     if cnt == 1:
#         print(1)
#     else:
#         print(0)
# func2([1, 52, 48], 3)
# func2([50, 42], 2)
# func2([4, 13, 63, 87], 4)

def fun2(arr, N): #4 13 63 87
    cnt = [0]*100
    check = 0
    for i in range(N):
        if cnt[100-arr[i]] == 1: #100-87 cnt[13]
            check = 1
            print(1)
            break
        cnt[arr[i]] = 1 #cnt[4][13][63] = 1
    if check == 0:
        print(0)
fun2([1, 52, 48], 3)
fun2([50, 42], 2)
fun2([4, 13, 63, 87], 4)