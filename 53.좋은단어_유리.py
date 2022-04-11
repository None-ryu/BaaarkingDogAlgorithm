# https://www.acmicpc.net/problem/3986
import sys

N = int(input())
cnt = 0
for _ in range(N):
    tmp = list(input()) # ABAB
    stack = []
    for txt in tmp:
        if not stack:
            stack.append(txt)
            continue

        if stack[-1] == txt:
            stack.pop()
        else:
            stack.append(txt)
    
    if len(stack) == 0:
        cnt+=1
print(cnt)