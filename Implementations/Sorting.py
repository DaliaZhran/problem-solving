""" *********************************** Sorting Algorithms *********************************** """
# * BUBBLE SORT
# * IDEA -> at every iteration, we sort an item from the end of the unsorted list.
# * KEYWORD -> Swapping adjecents, bubble to right
# Worst Case Time Complexity [ Big-O ]: O(n^2)
# Best Case Time Complexity [Big-omega]: Ω(n)
# Average Time Complexity [Big-theta]: Θ(n^2)
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


# * INSERTION SORT
# * IDEA -> at every iteration, we take an item from the unsorted part and insert it in the sorted part using shifting
# * KEYWORD -> Shifting, insert in sorted
# Worst Case Time Complexity [ Big-O ]: O(n^2)
# Best Case Time Complexity [Big-omega]: Ω(n)
# Average Time Complexity [Big-theta]: Θ(n^2)
# Space Complexity: O(1)
def insertionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]  # since we already stored the first i element in arr and we have a hole now
            j -= 1
        arr[j + 1] = temp


# * SELECTION SORT
# * IDEA -> at every iteration, we put the smallest item of the unsorted part in its correct position
# * KEYWORD -> Select min and swap with curr unsorted elem
# Worst Case Time Complexity [ Big-O ]: O(n^2)
# Best Case Time Complexity [Big-omega]: Ω(n^2)
# Average Time Complexity [Big-theta]: Θ(n^2)
# Space Complexity: O(1)
def selectionSort(arr):
    n = len(arr)
    #  traverse the array till n - 1 because at the end, the last element would be already sorted
    for i in range(n - 1):
        minElement = i
        # compare the current element with the unsorted part of the array
        for j in range(i + 1, n):
            if arr[minElement] > arr[j]:
                minElement = j
        arr[minElement], arr[i] = arr[i], arr[minElement]
    return arr


# * QUICK SORT
# * choose a pivot, get all smaller elements on the left, all bigger element on the right, and recurse
# * KEYWORD -> Pivot
# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: Ω(n*log n)
# Average Time Complexity [Big-theta]: Θ(n*log n)
# Space Complexity: O(n*log n) -> stack calls
def quickSort(arr):
    def partition(lb, ub):
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

    def quickSortDFS(lb, ub):
        if lb < ub:
            pivotLoc = partition(lb, ub)
            quickSortDFS(lb, pivotLoc - 1)
            quickSortDFS(pivotLoc + 1, ub)

    quickSortDFS(0, len(arr) - 1)


# * MERGE SORT
# * Make every element as a list and then merge upwards
# * KEYWORD -> lonley lists
# Worst Case Time Complexity [ Big-O ]: O(n*log n)
# Best Case Time Complexity [Big-omega]: Ω(n*log n)
# Average Time Complexity [Big-theta]: Θ(n*log n)
# Space Complexity: O(n)
def mergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        len_left = len(left)
        len_right = len(right)
        i = j = k = 0
        while i < len_left and j < len_right:
            if right[j] > left[i]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len_left:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len_right:
            arr[k] = right[j]
            j += 1
            k += 1


# * sorted [1, 3, 4, 5, 6, 7, 8]
nums = [3, 6, 8, 1, 7, 5, 4]
# bubbleSort(nums)
# selectionSort(nums)
# insertionSort(nums)
# quickSort(nums)
mergeSort(nums)
print(nums)