#https://www.acmicpc.net/problem/1406

def pringResult():  
    global linklist
    global word  
    global st
    stTmp = st
    result = []
    while True:
        result.append(word[stTmp])
        stTmp = linklist[stTmp]
        if stTmp == -1:
            break
        if linklist[stTmp] == -1:
            result.append(word[stTmp])
            break
    print(result, linklist, st, cursor)

word = list(input()) # a,b,c,d
linklist = [0] * len(word)
st = 0
for i in range(len(word)):
    linklist[i] = i+1
linklist[len(word)-1] = -1

cursor = len(word)-1
out = 0
N = int(input())
for i in range(N):
    cmd = list(input().split())
    print("------------cmd", cmd, "st", st)
    if cmd[0] == 'P':
        if out == 1:
            word.append(cmd[1])            
            linklist.append(-1)
            linklist[len(word)-1] = st
            st = len(word)-1            
            out = 0
        else:            
            word.append(cmd[1])
            tmp = linklist[cursor]
            linklist[cursor] = len(word)-1
            linklist.append(-1)
            linklist[len(word)-1] = tmp
            cursor = len(word)-1
    elif cmd[0] == 'B':
        if out == 1:

            #out = 0
            continue
        else:
            if cursor == 0:
                st = linklist[cursor] 
                linklist[cursor] = -2
                out = 1
                continue
            tmp = linklist[cursor]
            linklist[cursor] = -2
            cursor -= 1
            linklist[cursor] = tmp           
    elif cmd[0] == 'L':
        if cursor == 0:
            out = 1
            continue
        cursor -= 1
    elif cmd[0] == 'D':
        if cursor == len(word)-1:
            continue
        cursor += 1
    pringResult()

pringResult()

"""
[a x b]
ab
2
L
P x

[x a b]
ab
3
L
L
P x



출력조건
if st == -1:
    break[y]
xy
2
L
B
"""

"""
dmih
[dmx]
3
B
B
P x


[dx]
dmih
5
B
B
P x
L
B

[x]
dmih
6
B
B
P x
L
B
B

[yx]
dmih
8
B
B
P x
L
B
B
B
P y


dmih
10
B dmi 2
B dm 1
P x  dmx 2
L dmx    ['d', 'm', 'x'] [1, 4, -2, -2, -1] 1
B dx      ['d'] [-1, -2, -2, -2, -1] 0 
B x     0
B       0
P y xy  1
D
D
P z xyz 2

[dx]
dmx
2
L
B

커서가 안맞는 문제 해결못함
0123
abcx

커서가 1번에 있을때 L을 하면 3으로 이동해야하는 문제
a[x]b c
3[1]2-1

"""