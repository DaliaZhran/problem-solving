import math


def find_Kth_smallest_number(nums, k):
    # to handle duplicates, we will keep track of previous smallest number and its index
    previousSmallestNum, previousSmallestIndex = -math.inf, -1
    currentSmallestNum, currentSmallestIndex = math.inf, -1
    for i in range(k):
        for j in range(len(nums)):
            if nums[j] > previousSmallestNum and nums[j] < currentSmallestNum:
                # found the next smallest number
                currentSmallestNum = nums[j]
                currentSmallestIndex = j
            elif nums[j] == previousSmallestNum and j > previousSmallestIndex:
                # found a number which is equal to the previous smallest number; since numbers can repeat,
                # we will consider 'nums[j]' only if it has a different index than previous smallest
                currentSmallestNum = nums[j]
                currentSmallestIndex = j
                break  # break here as we have found our definitive next smallest number

        # current smallest number becomes previous smallest number for the next iteration
        previousSmallestNum = currentSmallestNum
        previousSmallestIndex = currentSmallestIndex
        currentSmallestNum = math.inf

    return previousSmallestNum


def main():

    print("Kth smallest number is: " + str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " + str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " + str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
