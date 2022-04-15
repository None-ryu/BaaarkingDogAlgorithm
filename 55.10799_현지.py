arr = list(input())
stack = []
stick = 0
for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(arr[i])
    else:
        if arr[i-1] == "(":
            stack.pop()
            stick += len(stack)
        else:
            stack.pop()
            stick += 1
print(stick)