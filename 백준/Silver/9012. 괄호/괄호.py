import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    str = input().strip()
    check = 0
    valid = True

    for j in str:
        if j=="(": 
            check += 1
        if j==")": 
            check -= 1

        if check<0: 
            valid=False 
            break
        
    if check!=0 or not valid: 
        print("NO")
    else: 
        print ("YES")