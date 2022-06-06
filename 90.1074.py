N, r, c = map(int, input().split())
num = 0
flag = -1
def visit(x, y, K):
    global r
    global c
    global num
    global flag
    a = x
    b = y
    if K == 0: 
        print(num)
        return 
    if r+1 <= y-2**(K-1):
        b = y-2**(K-1)
        if c+1 <= x-2**(K-1):
            a = x-2**(K-1)
            flag = 0
        else:
            flag = 1
    else:
        if c+1 <= x-2**(K-1):
            a = x-2**(K-1)
            flag = 2
        else:
            flag = 3
    num += ((2**(K-1))**2)*flag   
    visit(a, b, K-1)
visit(2**N, 2**N, N)