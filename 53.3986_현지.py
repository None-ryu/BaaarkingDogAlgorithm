N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
result = 0
for i in arr:
    Ast = 0
    Bst = 0
    call = []
    #able = 0
    for j in list(i):
        if j == "A":
            if Ast == 0:
                Ast += 1
                call.append(1)
            else:
                if len(call) != 0 and call[-1] == 1:
                    Ast -= 1
                    call.pop()
                else:
                    Ast += 1
                    call.append(1)
        if j == "B":
            if Bst == 0:
                Bst += 1
                call.append(2)
            else:
                if len(call) != 0 and call[-1] == 2:
                    Bst -= 1
                    call.pop()
                else:
                    Bst += 1
                    call.append(2)
    #if able == 0:
    if Ast == 0 and Bst == 0:
            result += 1
print(result)