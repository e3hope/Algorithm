def isEven(n):
    return 1 if n^1 == n+1 else 0

n = int(input())

print("Even" if isEven(n) == 1 else "Odd")