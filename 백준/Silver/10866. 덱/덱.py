import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
d = deque()

for i in range(n): 
    instruction = input().split()

    if instruction[0] == "push_front": d.appendleft(instruction[1])
    if instruction[0] == "push_back": d.append(instruction[1])
    if instruction[0] == "pop_front": 
        if len(d)==0: print(-1)
        else: print(d.popleft())
    if instruction[0] == "pop_back":
        if len(d)==0: print(-1) 
        else: print(d.pop())
    if instruction[0] == "size": 
        print(len(d))
    if instruction[0] == "empty":
        if len(d)==0: print(1)
        else: print(0)
    if instruction[0] == "front": 
        if len(d)==0:
            print(-1)
        else: print(d[0])
    if instruction[0] == "back":
        if len(d)==0:
            print(-1)
        else: print(d[-1])