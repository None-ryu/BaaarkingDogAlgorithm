n = 1
for i in range(3):
    N = int(input())
    n *= N
n = str(n)

result = [0]*10
for i in str(n):
    result[int(i)]+=1

for i in result:
    print(i)
