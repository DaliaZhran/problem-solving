# https://leetcode.com/problems/recover-binary-search-tree/
# feha iterative inorder hayel

# time -> O(n)
# space -> O(n)
class Solution:
    def recoverTree(self, root):
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        def find_two_swapped(nums):
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    # first swap occurence
                    if x == -1:
                        x = nums[i]
                    # second swap occurence
                    else:
                        break
            return x, y

        def recover(r, count):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover(r.left, count)
                recover(r.right, count)

        nums = inorder(root)
        x, y = find_two_swapped(nums)
        recover(root, 2)


# recursive
# time -> O(n)
# space -> O(H) -> recursive stack
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def find_two_swapped(root: TreeNode):
            nonlocal x, y, pred
            if root is None:
                return

            find_two_swapped(root.left)
            if pred and root.val < pred.val:
                y = root
                # first swap occurence
                if x is None:
                    x = pred
                # second swap occurence
                else:
                    return
            pred = root
            find_two_swapped(root.right)

        x = y = pred = None
        find_two_swapped(root)
        x.val, y.val = y.val, x.val
