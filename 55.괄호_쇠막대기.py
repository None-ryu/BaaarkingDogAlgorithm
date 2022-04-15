# https://www.acmicpc.net/problem/10799

N = input()
stack = []
open = False
cnt = 0

for txt in N:
    if txt == "(":
        stack.append(txt)
        open = True        
    elif txt == ")":
        if open is True:
            stack.pop()
            cnt += len(stack)                        
        else:
            stack.pop()
            cnt += 1
        open = False
print(cnt)
