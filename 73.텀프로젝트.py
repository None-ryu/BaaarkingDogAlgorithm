# https://www.acmicpc.net/problem/9466
import copy
import sys
sys.setrecursionlimit(3000000) 
input = sys.stdin.readline

T = int(input())
#selflist = set()
def recur(tmplist, st, friendnum): # 4 4
    # if checklist[friend[friendnum]] == -1:
    #     return 0
    #tmplist.add(friend[friendnum])
    tmplist += 1
    checklist[friend[friendnum]] = -1
    # 지가 지 뽑은 경우
    if st == friend[friend[friendnum]] == friend[friendnum]:            
        return 1#[st]
    # 지그 지 뽑은 애를 뽑은 경우
    if friend[friend[friendnum]] == friend[friendnum]:                
        return 0#[]
    # 사이클이 돈 후 시작값을 만나는 경우
    if st == friend[friendnum]:
        return tmplist
    else:             
        tmplist = recur(tmplist, st, friend[friendnum])        
        return tmplist
    
friend = []
for i in range(T):
    N = int(input())        
    # 3 1 3 7 3 4 6
    friend = [0]+list(map(int, input().split()))    
    cnt = 0
    #teamList = []
    checklist = copy.deepcopy(friend)
    for num in range(1, len(friend)):
        
        #tlist = recur(set([num]), checklist, num, num)
        #if checklist[num] != -1:
            tlist = recur(1, num, num)
            #teamList.append(tlist)
            if tlist == 0:
                cnt+=1

    # 예제1 [[], [], [3], [4, 7, 6, 4], [], [6, 4, 7, 6], [7, 6, 4, 7]]
    # 예제2 [[1], [2], [3], [4], [5], [6], [7], [8]]
    #print(teamList)
    # cnt = 0
    # for i in teamList:
    #     if len(i) == 0:
    #         cnt+=1
    print(cnt)



# 1
# 7
# 3 1 3 7 3 4 6

# 1 2 3 4 5 6
# 2 3 4 5 6 2

# 1 2 3 4 5
# 2 5 4 5 2


"""
# https://www.acmicpc.net/problem/9466
import copy
import sys
sys.setrecursionlimit(3000000) 
input = sys.stdin.readline

T = int(input())
def recur(st): # 4 4
    global cnt
    visited[st] = 1 
    next_st = friend[st]
    # 방문을 안했으면 방문
    if visited[next_st] == 0:
        recur(next_st)
    
    # 방문은 했는데 탐색이 안 끝난 경우
    elif done[next_st] == 0:
        cnt += 1     
        while next_st != st: # 본인과 가리키는 애가 동일한 경우
            next_st = friend[next_st]           
            cnt += 1     
            
    done[st] = 1

friend = []
done = []
cnt = 0
for i in range(T):
    N = int(input())        
    # 3 1 3 7 3 4 6
    friend = [0]+list(map(int, input().split()))    
    cnt = 0    
    visited = [0] * (N+1)
    done = [0] * (N+1)
    for num in range(1, len(friend)):
        if num == 6:
            print("test")
        if visited[num] == 0:
           recur(num)         
    print(N-cnt)
"""