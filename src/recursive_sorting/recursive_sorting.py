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
import math

def timsort( arr ):
    # skip merge if short list
    length = len(arr)
    if length < 64:
        return insertion_sort(arr)
    # make short, sorted runs
    run_length = math.ceil(length / 16)
    runs = []
    for i in range(0, len(arr), run_length):
        runs.append(insertion_sort(arr[i:i + run_length]))
    # merge runs
    while len(runs) > 1:
        runs[0] = merge(runs[0], runs.pop(1))
        # print(runs)
    return runs[0]

def insertion_sort( arr ):
    for i in range(1, len(arr)):
        # look backwards
        index = i
        for j in range(i - 1, -1, -1):
            # insert if less than
            if arr[i] < arr[j]:
                index = j
        if index != i:
            arr.insert(index, arr.pop(i))
    return arr

import random
import cProfile

def test_tim():
    test_arr = random.sample(range(10000),1024)
    test_arr_2 = test_arr.copy()

    # timsort
    pr = cProfile.Profile()
    pr.enable()
    timsort(test_arr)
    pr.disable()
    pr.print_stats()

    # merge sort
    pr = cProfile.Profile()
    pr.enable()
    merge_sort(test_arr_2)
    pr.disable()
    pr.print_stats()

test_tim()