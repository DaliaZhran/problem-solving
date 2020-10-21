""" *********************************** Sorting Algorithms *********************************** """

# Worst Case Time Complexity [ Big-O ]: O(n^2)
# Best Case Time Complexity [Big-omega]: O(n)
# Average Time Complexity [Big-theta]: O(n^2)
# Space Complexity: O(1)
def bubbleSort(arr):
    n = len(arr)
    # traverse the array from 0 to n - 1
    for i in range(n):
        flag = 0
        for j in range(n - 1 - i):  # last i are already in place
            if arr[j] > arr[j + 1]:  # swap if the 2 elements are not in order
                flag = 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not flag:
            break
    return arr


# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: O(n2)
# Average Time Complexity [Big-theta]: O(n2)
# Space Complexity: O(1)
def selectionSort(arr):
    n = len(arr)
    # traverse the array till n - 1 because at the end, the last element would be already sorted
    for i in range(n - 1):
        minElement = i
        # compare the current element with the unsorted part of the array
        for j in range(i + 1, n):
            if arr[minElement] > arr[j]:
                minElement = j
        if i != minElement:  # can be removed
            arr[minElement], arr[i] = arr[i], arr[minElement]
    return arr


def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub
    while start < end:
        while start < ub and arr[start] <= pivot:
            start += 1
        while end > lb and arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[lb] = arr[lb], arr[end]
    return end


# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: O(n*log n)
# Average Time Complexity [Big-theta]: O(n*log n)
# Space Complexity: O(n*log n) -> stack calls
def quickSort(arr):
    def quickSortDFS(arr, lb, ub):
        if lb < ub:
            pivotLoc = partition(arr, lb, ub)
            quickSortDFS(arr, lb, pivotLoc - 1)
            quickSortDFS(arr, pivotLoc + 1, ub)

    quickSortDFS(arr, 0, len(arr) - 1)


nums = [3, 6, 8, 1, 7, 5, 4]
# bubbleSort(nums)
# print(nums)
# selectionSort(nums)
# print(nums)
quickSort(nums)
print(nums)
