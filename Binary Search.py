# https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101


def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + ((r - l) >> 1)  # better than (r + l)//2 and l + (r+l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l + 1) // 2
        if target < nums[mid]:
            r = mid - 1
        else:
            l = mid

    return l if nums[l] == target else -1


def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if target < nums[mid]:
            r = mid
        else:
            l = mid + 1

    return l if nums[l] == target else -1


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 8))
