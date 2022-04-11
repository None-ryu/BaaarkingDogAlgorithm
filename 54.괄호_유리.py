# https://www.acmicpc.net/problem/9012

N = int(input())
for _ in range(N):
    tmp = list(input()) 
    stack = []
    for txt in tmp:
        if txt not in "()":
            continue

        if not stack or txt == "(":
            stack.append(txt)
            continue

        if txt == ")":
            if stack[-1] == "(":
                stack.pop()        
            else:
                stack.append(txt)
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")