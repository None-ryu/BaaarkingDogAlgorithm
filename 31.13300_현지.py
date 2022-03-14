import math
total, full = map(int, input().split())
female = [0]*7
male = [0]*7
for _ in range(total):
    sex, grade = map(int, input().split())
    if sex == 0:
        female[grade] += 1
    if sex == 1:
        male[grade] += 1
room = 0
for i in female:
    room += math.ceil(i/full)
for i in male:
    room += math.ceil(i/full)
print(room)