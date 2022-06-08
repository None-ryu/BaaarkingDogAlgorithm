# https://www.acmicpc.net/problem/1074
result = 0
def func(n, x, y):
    global result    
    if n<1:                
        return
    cnt = 0
    if x<=n: #1,3사분면
        if y<=n: #1분면
            cnt = 0
        else: #3분면
            cnt = 2
    else: #2,4 사분면
        if y<=n: #2분면
            cnt = 1
        else: #4분면
            cnt = 3    
    
    #print("x:", x," y:", y)
    if x>n:
        x = x-n
    if y>n:
        y = y-n   
    tmp = (n*n)*cnt         
    #print("N:",n, "분면:", cnt+1, "tmp", tmp     )     
    result += tmp    
    func(n//2, x, y)

n,y,x = map(int, input().split()) #2 3 1
func( (2**n)//2, x+1, y+1) # 2 2 4
print(result)