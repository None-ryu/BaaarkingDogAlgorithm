import sys
input = sys.stdin.readline
N = int(input())
if N < 3:
    print(0)
    sys.exit()
student = sorted(list(map(int, input().split())))
answer = 0
for i in range(N-2):
    low = i+1
    high = N-1
    goal = student[i]
    tmp = N-1
    while low < high:
        if goal+student[low]+student[high] == 0:
            if student[low] == student[high]:
                answer += high - low
            else:
                if tmp > high:
                    tmp = high
                while student[tmp] == student[high]:
                    tmp -= 1
                answer += high-tmp
            low += 1
        if goal+student[low]+student[high] < 0:
            low += 1
        elif goal+student[low]+student[high] > 0:
            high -= 1
print(answer)