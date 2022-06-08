# https://www.acmicpc.net/problem/10804

arr = [i for i in range(20+1)] # 0~20
for i in range(10):
    a, b = map(int, input().split()) #5 10

    tmparr = []
    # [10,9,8,7,6,5] 뒤집는다.
    for tmp in range(b, a-1, -1):
        tmparr.append(arr[tmp])
    
    check =0  
    for j in range(a, b+1):
        arr[j] = tmparr[check]
        check += 1
    print(*arr)
arr.pop(0)
print(*arr)