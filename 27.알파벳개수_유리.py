n = 1
for i in range(3):
    N = int(input())
    n *= N
n = str(n)

result = [0]*10
for i in n: # 14111  0 4 0 0 1 .....
    result[int(i)]+=1
    
for i in result:
    print(i)