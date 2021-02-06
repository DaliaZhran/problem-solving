# https://leetcode.com/problems/strobogrammatic-number-ii/


# Recursive
# Time: O()
# Space: O()
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(m):
            if m == 0:
                return [""]
            if m == 1:
                return ["0", "1", "8"]

            curr_list = helper(m - 2)
            curr_res = []

            for s in curr_list:
                if m != n:
                    curr_res.append("0" + s + "0")

                curr_res.append("1" + s + "1")
                curr_res.append("6" + s + "9")
                curr_res.append("9" + s + "6")
                curr_res.append("8" + s + "8")
            return curr_res

        return helper(n)


# Iterative
# Time: O()
# Space: O()
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = ["0", "1", "8"] if n % 2 else [""]
        if n < 2:
            return res

        while n > 1:
            cur = res
            res = []
            for s in cur:
                if n > 3:
                    res.append("0" + s + "0")

                res.append("1" + s + "1")
                res.append("6" + s + "9")
                res.append("9" + s + "6")
                res.append("8" + s + "8")

            n -= 2

        return res