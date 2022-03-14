case = int(input())
for _ in range(case):
    cnt = 0
    str1, str2 = input().split()
    str1 = list(str1)
    str2 = list(str2)
    if len(str1) != len(str2):
        print("Impossible")
        continue
    for i in range(len(str1)):
        if str1[i] in str2:
            str2.remove(str1[i])
            cnt += 1
    if cnt != len(str1):
        print("Impossible")
    else:
        print("Possible")