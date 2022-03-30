import sys
input =  sys.stdin.readline
stack = []
call = int(input())
for i in range(call):
    arr = list(input().split())
    if "push" in arr:
        stack.append(arr[1])
    if "pop" in arr:
        if len(stack) != 0:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)
    if "size" in arr:
        print(len(stack))
    if "empty" in arr:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if "top" in arr:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

# from collections import deque
# stack = deque([])
# call = int(input())
# X = -1
# for i in range(call):
#     arr = list(input().split())
#     if "push" in arr:
#         stack.append(arr[1])
#         X = arr[1]
#     if "pop" in arr:
#         if X != 0:
#             print(stack.pop())
#             if len(arr) != 0:
#                 X = stack[-1]
#             else:
#                 X = -1
#         else:
#             print(-1)
#     if "size" in arr:
#         print(len(stack))
#     if "empty" in arr:
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     if "top" in arr:
#         if len(stack) != 0:
#             print(stack[-1])
#         else:
#             print(-1)