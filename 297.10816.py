import sys
input = sys.stdin.readline
N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
number = list(map(int, input().split()))
answer = []
def find(num, st, ed):
    global answer
    if st > ed:
        answer.append(0)
        return
    else:
        if card[(st+ed)//2] < num:
            find(num, (st+ed)//2+1, ed)
        elif card[(st+ed)//2] == num:
            low = 0
            high = (st+ed)//2-1
            start = 0
            while True:
                if low < 0 or high < 0:
                    start = 0
                    break
                if high < low:
                    if card[high] != card[low]:
                        start = low
                    else:
                        start = high
                    break
                if card[(low+high)//2] < num:
                    low = (low+high)//2+1
                elif card[(low+high)//2] == num:
                    high = (low+high)//2-1
            low = (st+ed)//2+1
            high = N-1
            end = 0
            while True:
                if high > N-1 or low > N-1:
                    end = N-1
                    break
                if high < low:
                    if card[high] != card[low]:
                        end = high
                    else:
                        end = low
                    break
                if card[(low+high)//2] > num:
                    high = (low+high)//2-1
                elif card[(low+high)//2] == num:
                    low = (low+high)//2+1
            answer.append(end-start+1)
            return
        elif card[(st+ed)//2] > num:
            find(num, st, (st+ed)//2-1)
for i in number:
    find(i, 0, N-1)
print(*answer)