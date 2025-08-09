n = int(input())

if n>20 or n<0:
    exit()

def getNum(n): 
    if n<=1: 
        return n
    return getNum(n-1)+getNum(n-2)

print(getNum(n))