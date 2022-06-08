# https://www.acmicpc.net/problem/2630
import sys
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, list(input().split()))))

total0 = 0
total1 = 0

def checkPaper(stx, endx, sty, endy, num):    
    global total0, total1
    for yy in range(sty, endy):
        for xx in range(stx, endx):            
            if graph[yy][xx] != graph[sty][stx]:
                recur(stx, sty, num//2)
                return False

    if graph[sty][stx] == 0:
        total0+=1
    elif graph[sty][stx] == 1:
        total1+=1
    return True

def recur(sx, sy, num):    
    tmpx = sx
    for y in range(2):                
        for x in range(2):
            checkPaper(sx, sx+num//2, sy, sy+num//2, num) 
            #print("test", sx, sx+num//3, sy, sy+num//3, num)
            sx +=num//2
        sx = tmpx
        sy += num//2

   

for y in range(N):
    for x in range(N):
        if graph[y][x] != graph[0][0]:            
            recur(0, 0, N)            
            print(total0)
            print(total1)
            sys.exit()

if graph[0][0] == 0:
    total0+=1
elif graph[0][0] == 1:
    total1+=1
print(total0)
print(total1)