# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Normal Backtracking
# Time: O(3^N * 4^M)
# Space: O(3^N * 4^M)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(idx, candidate):
            if idx == length:
                res.append(candidate)
                return

            for next_char in mapping[digits[idx]]:
                candidate += next_char
                backtrack(idx + 1, candidate)
                candidate = candidate[0:-1]

        mapping = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        length = len(digits)
        res = []
        if digits:
            backtrack(0, "")
        return res


# Pythonic way
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ret = []
        self.dfs(m, digits, "", ret)
        return ret

    def dfs(self, m, digits, path, ret):
        if not digits:
            ret.append(path)
            return
        for c in m[digits[0]]:
            self.dfs(m, digits[1:], path + c, ret)


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8067/Python-easy-to-understand-backtracking-solution.
