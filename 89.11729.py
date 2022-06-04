N = int(input())
def stack(x, y, k):
    if k == 1:
        print(x, y, sep=" ")
        return
    stack(x, 6-x-y, k-1)
    print(x, y, sep=" ")
    stack(6-x-y, y, k-1)
print(2**N-1)
stack(1, 3, N)