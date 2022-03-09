# https://www.acmicpc.net/problem/10808
# word = input()
# result = []
# for num in range(97, 123):
#     alpha = chr(num)
#     cnt = 0
#     for w in word:
#         if alpha == w:
#             cnt+=1
#     result.append(cnt)
# print(*result)


# 97 a
# 122  z

word = input()
result = [0]*26
for w in word:
    result[ord(w)-97] += 1
print(*result)