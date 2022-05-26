# N~1 출력
def recur(N):
    print(N)
    if N > 1:
        recur(N-1)
#recur(10)

# N~1 합
total = 0
def recurSum(N):   
    global total 
    total += N
    if N > 1:
        recurSum(N-1)    
recurSum(3)
print(total)