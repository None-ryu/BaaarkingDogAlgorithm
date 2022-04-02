import sys
input = sys.stdin.readline
N = int(input())
queue = []
for _ in range(N):
    command = list(input().split())
    if "push" in command:
        queue.append(command[1])
    if "pop" in command:
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    if "size" in command:
        print(len(queue))
    if "empty" in command:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if "front" in command:
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    if "back" in command:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)