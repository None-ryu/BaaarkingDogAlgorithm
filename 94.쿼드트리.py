# https://www.acmicpc.net/problem/1992
import sys
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = ""

def checkPaper(stx, endx, sty, endy, num):    
    global result    
    for yy in range(sty, endy):
        for xx in range(stx, endx):                  
            if graph[yy][xx] != graph[sty][stx]:
                recur(stx, sty, num//2)
                return False
    result+=str(graph[sty][stx])
    return True

def recur(sx, sy, num): 
    global result   
    tmpx = sx
    result+="("
    for y in range(2):                
        for x in range(2):
            checkPaper(sx, sx+num//2, sy, sy+num//2, num) 
            sx +=num//2
        sx = tmpx
        sy += num//2

    result+=")"

for y in range(N):
    for x in range(N):
        if graph[y][x] != graph[0][0]:            
            recur(0, 0, N) 
            print(result)
            sys.exit()
print(str(graph[0][0]))

