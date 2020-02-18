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
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
