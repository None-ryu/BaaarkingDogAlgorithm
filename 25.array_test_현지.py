arr1 = [10, 20, 30]
def insert(number, object):
    arr1.append(0)
    for i in range(len(arr1), 1, -1):
        if i == number:
            break
        arr1[i-1] = arr1[i-2]
    arr1[number] = object
    print(*arr1, "/", len(arr1), sep=" ")
arr2 = [10, 50, 40, 30, 70, 20]    
def erase(number):
    for i in range(number+1, len(arr2)):
        arr2[i-1] = arr2[i]
    arr2.pop()
    print(*arr2, "/", len(arr2), sep=" ")
insert(3, 40)
insert(1, 50)
insert(0, 15)
erase(4)
erase(1)
erase(3)