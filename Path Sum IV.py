# https://leetcode.com/problems/path-sum-iv/


# Use Map and preorder traversal
# Time : O(N) for constructing the map and O(N) for traversing the tree
# Space : O(N) for the map and O(H) for the traverse
class Solution:
    result = 0

    def pathSum(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for num in nums:
            mp[num // 10] = num % 10

        self.traverse(nums[0] // 10, 0, mp)
        return self.result

    def traverse(self, root, prev_sum, mp):
        val = mp[root]
        level = root // 10
        pos = root % 10
        left = (level + 1) * 10 + (2 * pos - 1)
        right = (level + 1) * 10 + (2 * pos)

        curr_sum = prev_sum + val
        if left not in mp and right not in mp:
            self.result += curr_sum

        if left in mp:
            self.traverse(left, curr_sum, mp)
        if right in mp:
            self.traverse(right, curr_sum, mp)
