# https://www.acmicpc.net/problem/2504
import sys
N = input()
stack = []

for txt in N:
    if txt == "(" or txt == "[" :
        stack.append(txt)            
    elif txt == ")": 
        try:
            tmp = stack.pop()
        except:
            stack = 0
            break
        if tmp == "(":
            stack.append(2)
        elif str(tmp).isdigit() is False:
            stack = 0
            break
        else:  
            try:          
                while str(stack[-1]).isdigit():
                    tmp += stack.pop()
                tmp = tmp*2            
                tmp2 = stack.pop()  
                if tmp2 == "[":
                    stack = 0
                    break
            except:
                stack = 0
                break 

            stack.append(tmp)
    elif txt == "]": 
        try:
            tmp = stack.pop()
        except:
            stack = 0
            break
        if tmp == "[":
            stack.append(3)
        elif str(tmp).isdigit() is False:
            stack = 0
            break
        else:            
            try:
                while str(stack[-1]).isdigit():
                    tmp += stack.pop()   
                tmp = tmp*3
                tmp2 = stack.pop()  
                if tmp2 == "(":
                    stack = 0
                    break 
            except:
                stack = 0
                break
              
            stack.append(tmp)
#print(stack)    
if stack == 0:
    print(stack)  
else:
    try:
        print(sum(stack))
    except:
        print(0)  

# 예외 [[]) 정답0 
# 예외 )) try except 처리