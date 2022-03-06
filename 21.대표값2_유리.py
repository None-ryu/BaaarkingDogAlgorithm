# https://www.acmicpc.net/problem/2587

num = []
for i in range(5):
    N = int(input())
    num.append(N)
num.sort()
print(sum(num)//5)
print(num[2])
