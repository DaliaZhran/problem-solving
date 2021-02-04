# General Template
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space)  # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


# Template 1: find a target in the search space
def binary_search(array, target) -> int:
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1  # not found


# Template 2: find smallest number greater than a target
def binary_search(array, target) -> int:
    left, right = 0, len(array) - 1
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left  # left = right


# Template 3: find greatest number smaller than a target
def binary_search(array, target) -> int:
    left, right = 0, len(array) - 1
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid
    return left  # left = right


# Template 4: find smallest range that a number lies in (to check for smallest difference for example)
def binary_search(array, target) -> int:
    left, right = 0, len(array) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if array[mid] > target:
            right = mid
        else:
            left = mid
    # now we need to check the left and right boundaries
    return left if abs(array[left] - target) < abs(array[right] - target) else right