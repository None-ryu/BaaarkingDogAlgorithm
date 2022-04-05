from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input().replace("RR", "")
    n = int(input())
    array = list(input().strip().split(","))
    for i in range(len(array)):
        if array[i] != "[]":
            array[i] = array[i].replace("[", "")
            array[i] = int(array[i].replace("]", ""))
        else:
            array = []
            break
    array = deque(array)
    reve = 0
    able = 0
    for i in p:   
        if i == "R":
            reve += 1
        if i == "D":
            if len(array) == 0:
                print("error")
                able = 1
                break
            else:
                if reve%2 != 0:
                    array.pop()
                else:
                    array.popleft()
    if reve%2 != 0:
        array.reverse()
    if able == 0:
        print("[", end="")
        for i in range(len(array)):
            if i != len(array)-1:
                print(array[i], end=",")
            else:
                print(array[i], end="")
        print("]")