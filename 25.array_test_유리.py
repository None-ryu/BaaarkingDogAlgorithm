# 1 (6) [2] 3  [4] 5

# 1 번째 6을 넣는다
def insert(idx, num, arr):
    arr.append(num)
    for i in range(len(arr)-2, idx-1, -1):
        arr[i+1] = arr[i] 
    arr[idx] = num

def erase(idx, arr):
    for i in range(idx, len(arr)-1):
        arr[i]=arr[i+1]
    arr.pop()

# 0 1 () 2 3 4
def insertTest():
    arr = [10,20,30]
    insert(3, 40, arr)
    print(arr)
    insert(1, 50, arr)
    print(arr)
    insert(0, 15, arr)
    print(arr)

def eraseTest():
    arr = [10, 50, 40, 30, 70, 20]
    erase(4, arr)
    print(arr)
    erase(1, arr)
    print(arr)
    erase(3, arr)
    print(arr)

insertTest()
eraseTest()