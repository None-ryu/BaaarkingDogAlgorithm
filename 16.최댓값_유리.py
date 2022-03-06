# https://www.acmicpc.net/problem/2562

maxNum = 0
maxIndex = 0
for i in range(9):
    num = int(input())
    if maxNum < num:
        maxNum = num
        maxIndex = i+1
print(maxNum)
print(maxIndex)