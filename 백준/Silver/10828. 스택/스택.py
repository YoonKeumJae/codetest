import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n): 
    instruction = sys.stdin.readline().split()
    if instruction[0]=="push": 
        stack.append(instruction[1])
    if instruction[0]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1]) 
            stack.pop()
    if instruction[0]=="size":
        print(len(stack))
    if instruction[0]=="empty":
        if len(stack)==0:
            print(1)
        else: print(0)
    if instruction[0]=="top":
        if len(stack)==0:
            print(-1)
        else: print(stack[-1])


    