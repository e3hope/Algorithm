def find(nums, n):
    leftMax = [None] * n
    leftMax[0] = nums[0]
 
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], nums[i-1])
 
    rightMin = [None]*n
    rightMin[n-1] = nums[n-1]
 
    for i in range(n-2, -1, -1):
        rightMin[i] = min(rightMin[i+1], nums[i])
    
    for i in range(1, n-1):
        if leftMax[i-1] <= nums[i] and nums[i] <= rightMin[i+1]:
            return i
    return -1

nums = [5, 1, 4, 3, 6, 8, 10, 7, 9]
n = len(nums)
print(find(nums, n))