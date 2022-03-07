N = int(input())
Nlist = list(map(int, input().split()))
Yrate = 0
Mrate = 0
for i in Nlist:
    Yrate += (i//30+1)*10
    Mrate += (i//60+1)*15
if Yrate < Mrate:
    print("Y", Yrate)
if Yrate > Mrate:
    print("M", Mrate)
if Yrate == Mrate:
    print("Y", "M", Yrate)