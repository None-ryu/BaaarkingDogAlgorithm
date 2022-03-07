people = []
for _ in range(9):
    people.append(int(input()))
visited = [False]*9
result = []
def dfs(depth, st):
    if depth == 7 and sum(result) == 100:
        result.sort()
        for i in result:
            print(i)
        return
    for i in range(st, 9):
        if visited[i]:
            continue
        visited[i] = True
        result.append(people[i])
        dfs(depth+1, i+1)
        result.pop()
        visited[i] = False
dfs(0, 0)