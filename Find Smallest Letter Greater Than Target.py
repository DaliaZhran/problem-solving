# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# binary search template II
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n  # n because we want the one element next to our target
        while l < r:
            mid = l + (r - l) // 2  # biased to left element
            if letters[mid] <= target:  # we do not want to return the target that is why we used =
                l = mid + 1
            else:
                r = mid  # we do not skip the mid here because it may be the greater letter after out target

        return letters[l % n]  # % because problem makes the array like if its circular


# another implementation Template I
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        if n == 0:
            return None

        low = 0
        high = n - 1
        # If it can not be found, must be the first element (wrap around)
        result = 0

        while low <= high:
            mid = low + (high - low) // 2
            if letters[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return letters[result]