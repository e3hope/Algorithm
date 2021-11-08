def cal(n):
    num = bin(n)
    num = num[2:]
    answer = 0
    length = len(str(num)) - 1
    for b in range(length,0,-1):
        if num[b] == str(0):
            answer = n + 2**(length-b)
            break
    if not answer:
        answer = 0
    return answer

n = int(input())
print("Input:" + str(n), "Output:" + str(cal(n)), sep='\n')
