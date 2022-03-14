str1 = list(input())
str2 = list(input())
result = 0
if len(str1) > len(str2):
    for i in range(len(str2)):
        if str2[i] in str1:
            str1.remove(str2[i])
        else:
            result += 1
    print(result+len(str1))
else:
    for i in range(len(str1)):
        if str1[i] in str2:
            str2.remove(str1[i])
        else:
            result += 1
    print(result+len(str2))