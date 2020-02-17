# STRETCH: implement Linear Search				
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1     # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty
        
    low = 0
    high = len(arr)-1

    while True:
        middle = (low+high) // 2
        if target == arr[middle]:
            return middle
        if low == high:
            break
        if target > arr[middle]:
            low = middle
        if target < arr[middle]:
            high = middle
    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
    
    middle = (low+high)//2

    if len(arr) == 0:
        return -1 # array empty
    
    if target == arr[middle]:
        return middle
    if low == high:
        return -1
    if target > arr[middle]:
        return binary_search_recursive(arr, target, middle, high)
    if target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle)
