# https://www.acmicpc.net/problem/1629
import sys
sys.setrecursionlimit(10 ** 6)
A, B, C = map(int, input().split())
print(pow(A, B, C))
tmp = A
num = 1
Bcheck = B

def recur(mynum):
    global A, B, C, tmp, num, Bcheck
    if mynum == 1:
        tmp = tmp*A%C
    while True:
        if num*2 >Bcheck:
            tmp = tmp % C
            break
        num = num*2
        tmp = (tmp**2)%C
        
        
    mynum = mynum-num
    if mynum>0:
        Bcheck -= num
        num = 1    
        if mynum>1:
            tmp = tmp * A
        mynum = recur(mynum)        
if B>1:
    recur(B)
else:
    tmp = A%C
print(tmp)

#반례 11 6 54 => 37