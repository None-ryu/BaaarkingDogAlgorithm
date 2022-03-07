# https://www.acmicpc.net/problem/1267

N = int(input())
num = list(map(int, input().split()))
Y = 0
M = 0

for i in num:
    Y += i//30 * 10
    Y+=10
    
    M += i//60 * 15
    M+=15
if Y==M:
    print("Y M", Y)
elif Y<M:
    print("Y", Y)
else:
    print("M", M)