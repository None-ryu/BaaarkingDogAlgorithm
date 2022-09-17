# https://www.acmicpc.net/problem/2143
import sys
input = sys.stdin.readline
N = int(input())
A = int(input())
arrA = list(map(int, input().split()))
B = int(input())
arrB = list(map(int, input().split()))

arrASum = []
for num1 in range(len(arrA)):    
    tmp = 0
    for num2 in range(num1, len(arrA)):
        tmp += arrA[num2]
        arrASum.append(tmp)
arrASum.sort()
#print(arrASum)

dictArr = {}
arrBSum = []
for num1 in range(len(arrB)):    
    tmp = 0
    for num2 in range(num1, len(arrB)):
        tmp += arrB[num2]
        arrBSum.append(tmp)
        
        if tmp in dictArr:
            dictArr[tmp] = dictArr[tmp]+1
        else:
            dictArr[tmp] = 1
arrBSum.sort()
#print(arrBSum)
#print("dictArr: ", dictArr)


answer = 0
for i in arrASum:
    target = N-i # 이 수가 있는지 보자 
    
    if target in dictArr:
        answer += dictArr[target]
print(answer)

"""
arrASum = []
for idx1 in range(len(arrA)):
    tmp = []
    for arrs in arrASum:
        tmp.append(arrs+arrA[idx1])
    arrASum += tmp
    arrASum.append(arrA[idx1])
arrASum.sort()
print(arrASum)
"""