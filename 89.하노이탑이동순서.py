# https://www.acmicpc.net/problem/11729

# 원판n개를 a번 기둥에서 b번 기둥으로 옮기는 방법
def func(a, b, n):
    if n==1:        
        print(a, b) 
        return
    # 맨밑에 아이를 목표지점으로 옮기려면 
    # 그위에 있는 애들을 목표지점과 시작지점이아닌곳으로 옮겨야함

    # 다른애를 치운다
    func(a, 6-a-b, n-1) # 1번 (1,2,2) (1,3,1) 1->3 5번 (2,1,1) 2->1
    # 목표지점으로 옮긴다
    print(a, b) # 2번  1->2  3번 1->3  6번 2->3
    # 치운 애를 목표지점으로
    func(6-a-b, b, n-1)# 4번(2,3,2)   7번 (1,3,1) 1->3
num = int(input())
print(2**num-1)
func(1, 3, num)