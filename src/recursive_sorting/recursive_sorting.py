# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # uncomment if input lists should not be modified
    # arrA = arrA.copy()
    # arrB = arrB.copy()
    merged_arr = []
    while arrA and arrB:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    merged_arr.extend(arrA)
    merged_arr.extend(arrB)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    length = len(arr)
    if length > 1:
        half = length // 2
        low = merge_sort(arr[:half])
        high = merge_sort(arr[half:])
        return merge(low, high)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, half, stop):
    i, j = 0, 0
    # debug = arr[start:stop+1]
    while half + i <= stop and start + j < half + i:
        if arr[half + i] < arr[start + j]:
            arr.insert(start + j, arr.pop(half + i))
            i += 1
        j += 1
    # print(f'{debug} -> {arr[start:stop+1]}')
    return arr

def merge_sort_in_place(arr, start=0, stop=None):
    if stop == None:
        stop = len(arr) - 1
    length = stop - start + 1
    if length > 1:
        half = start + length // 2
        merge_sort_in_place(arr, start, half - 1)
        merge_sort_in_place(arr, half, stop)
        merge_in_place(arr, start, half, stop)
    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
