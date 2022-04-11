# https://www.acmicpc.net/problem/4949
from collections import deque
import sys
input = sys.stdin.readline


while True:
    txt = list(input())
    #print(txt)
    #print()

    if len(txt) == 2 and txt[0] == ".":        
        break
    dq = deque()
    result = True
    for t in txt:
        if t == "(":
            dq.append("(")
        elif t == "[":
            dq.append("[")
        elif t == "]":
            if len(dq)>0 and dq[-1] == "[":
                dq.pop()
            else:
                print("no")
                result = False
                break
        elif t == ")":
            if len(dq)>0 and dq[-1] == "(":
                dq.pop()
            else:
                print("no")
                result = False
                break

    if result is True:
        if len(dq) == 0:
            print("yes")
        else:
            print("no")
            
                
        