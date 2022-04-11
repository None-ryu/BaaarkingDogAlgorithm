T = int(input())
for _ in range(T):
    arr = list(input())
    stack = []
    for i in arr:
        if len(stack) == 0:
            if i == "(":
                stack.append(i)
                continue
            else:
                stack.append(i)
                break
        if stack[-1] != i and i == ")":
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")