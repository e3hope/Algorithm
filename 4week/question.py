def reorder(array, n):
    j = 0 
    for i in range(n):
        if array[i] != 0:
            array[j] = array[i]
            j+=1 
    for i in range(j,n):
        array[i] = 0 
    # code
array = [6, 0, 8, 2, 3, 0, 4, 0, 1]
n = len(array)
reorder(array, n)
print(array)