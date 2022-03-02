# cards = []
# for i in range(1, 21):
#     cards.append(i)
# for _ in range(10):
#     st, ed = map(int, input().split())
#     for i in range(ed-st+1):
#         if ed-st == 1:
#             cards[ed] = cards[st]
#             cards[st] = cards[ed]
#             break
#         cards[st+i] = cards[ed-i]
#         cards[ed-i] = cards[st+i]
# print(*cards)

cards = []
for i in range(21):
    cards.append(i) #0~20
for _ in range(10):
    st, ed = map(int, input().split()) #5, 10 #1, 20
    if ed-st == 1:
        aed = cards[ed]
        ast = cards[st]
        cards[st] = aed
        cards[ed] = ast
    else:
        for i in range((ed-st)//2+1): #range(3) #range(17)
            newst = cards[st+i] #5, 6, 7 #1, 2, 3, ... 17
            newed = cards[ed-i] #10, 9, 8 #20, 19, 18, ... 4
            cards[st+i] = newed #10, 9, 8 #20, 19, 18, ... 4
            cards[ed-i] = newst #5, 6, 7 #1, 2, 3, ... 17
cards.pop(0)
print(*cards)          

# cards = []
# for i in range(1, 21):
#     cards.append(i)
# for _ in range(10):
#     st, ed = map(int, input().split())
