import sys

def find(nums, n):
    max = sys.maxsize
    min = -sys.maxsize - 1
    leftMax = [0] * n
    rightMin = [0] * n
    answer = []

    leftMax[0] = min
 
    for i in range(1, n):
        if leftMax[i-1] > nums[i-1]: 
            leftMax[i] = leftMax[i-1]
        else:
            leftMax[i] = nums[i-1]

    rightMin[n-1] = max
 
    for i in range(n-2, 0, -1):
        if rightMin[i+1] > nums[i+1]:
            rightMin[i] = nums[i+1]
        else:
            rightMin[i] = rightMin[i+1]
    
    sts = 0
    
    for i in range(n):
        if leftMax[i] < nums[i] and rightMin[i] > nums[i]:
            print(i,end=" ")
            sts = 1
    
    if sts == 0:
        print('-1')
    else:
        return answer

nums = list(map(int, input().split()))
n = len(nums)
find(nums, n)
