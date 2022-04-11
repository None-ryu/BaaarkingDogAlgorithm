arr = []
while True:
    line = input()
    arr.append(line)
    if line == ".":
        break
for i in range(len(arr)-1):
    sentence = list(arr[i])
    smbr = 0
    bibr = 0
    state = []
    able = 0
    for j in sentence:
        if j == "(":
            smbr += 1
            state.append(1)
        if j == "[":
            bibr += 1
            state.append(2)
        if j == ")":
            if len(state) == 0:
                print("no")
                able = 1
                break
            elif state[-1] == 1:
                smbr -= 1
                state.pop()
            else:
                print("no")
                able = 1
                break
        if j == "]":
            if len(state) == 0:
                print("no")
                able = 1
                break            
            elif state[-1] == 2:
                bibr -= 1
                state.pop()
            else:
                print("no")
                able = 1
                break
    if able == 0:
        if smbr == 0 and bibr == 0:
            print("yes")
        else:
            print("no")