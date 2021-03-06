from typing import List

"""
An element in a sorted array can be found in O(log n)
time via binary search. But suppose we rotate an
ascending order sorted array at some pivot unknown
to you beforehand. So for instance, 1 2 3 4 5 might
become 3 4 5 1 2. Devise a way to find an element
in the rotated array in O(log n) time.
"""

"""
Steps:
Find the pivot
search the element in two subarray,  low -> pivot, pivot+1 -> high
"""


def pivotedBinarySearch(arr: List[int], n: int, key: int) -> int:
    pivot: int = findPivot(arr, 0, n - 1)

    if pivot == -1:
        return binarySearch(arr, 0, n - 1, key)

    if arr[pivot] == key:
        return pivot

    if arr[0] <= key:
        return binarySearch(arr, 0, pivot - 1, key)
    return binarySearch(arr, pivot + 1, n - 1, key)


def findPivot(arr: List[int], low: int, high: int) -> int:
    # base case
    if high < low:
        return -1
    if high == low:
        return low

    mid: int = (low + high) // 2

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid

    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1

    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)

    return findPivot(arr, mid + 1, high)


def binarySearch(arr: List[int], low: int, high: int, key: int) -> int:
    mid: int = (low + high) // 2

    if low > high:
        return -1

    if arr[mid] == key:
        return mid

    if arr[mid] > key:
        return binarySearch(arr, low, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, high, key)


arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr1)
key = 3
print("Index of the element is : ", pivotedBinarySearch(arr1, n, key))
