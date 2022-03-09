# def func2(arr, N):
#     for x in range(len(arr)):
#         for y in range(x+1, len(arr)):
#             if arr[x]+arr[y] == 100:
#                 print(1)
#                 return
#     print(0)
# func2([1, 52, 48], 3)
# func2([50, 42], 2)
# func2([4, 13, 63, 87], 4)

# def func3(arr, N):
#     total = sum(arr)
#     for x in range(len(arr)):
#         total -= arr[x]
# func3([1, 52, 48], 3)
# func3([50, 42], 2)
# func3([4, 13, 63, 87], 4)

# 1 2 (3) 4 (5) 6 (7) 8 9 10

def func4(arr, N):
    num = [0 for _ in range(101)]
    for tmp in arr:
        num[tmp] = 1
    for tmp in arr:
        if tmp != 100-tmp and num[100 - tmp] ==1:
            return 1
    return 0

print(func4([1, 52, 48], 3))
print(func4([50, 42], 2))
print(func4([4, 13, 63, 87], 4))