N = int(input())
cnt = 0
def minus():
    global cnt
    if N-cnt == 0:
        return
    print(N-cnt)
    cnt += 1
    minus()
minus()
cnt = 0
total = 0
def plus():
    global cnt
    global total
    if N-cnt == 0:
        print(total)
        return
    total += N-cnt
    cnt += 1
    plus()
plus()