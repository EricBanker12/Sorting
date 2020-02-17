# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        if cur_index != smallest_index:
            temp = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop through pairs
    for i in range(0, len(arr) - 1):
        # swap pairs if b < a
        j = i + 1
        if arr[j] < arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            # repeat until sorted/no-swaps
            return bubble_sort(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if not arr:
        return arr
    # get maximum
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if num > maximum:
            maximum = num
    # count keys
    table = [0 for c in range(maximum + 1)]
    for num in arr:
        table[num] += 1
    # make sorted array
    sorted_arr = []
    for i in range(len(table)):
        if table[i]:
            sorted_arr.extend([i for c in range(table[i])])
    return sorted_arr