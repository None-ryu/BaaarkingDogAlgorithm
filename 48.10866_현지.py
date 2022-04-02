from collections import deque
import sys
input = sys.stdin.readline
queue = deque([])
N = int(input())
for _ in range(N):
    command = list(input().split())
    if "push_front" in command:
        queue.appendleft(command[1])
    if "push_back" in command:
        queue.append(command[1])
    if "pop_front" in command:
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    if "pop_back" in command:
        if len(queue) != 0:
            print(queue.pop())
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