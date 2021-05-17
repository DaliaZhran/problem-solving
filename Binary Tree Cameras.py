# https://leetcode.com/problems/binary-tree-cameras/https://leetcode.com/problems/binary-tree-cameras/

"""
Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.


Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# PostOrder DFS
# Time Complexity: O(N), where N is the number of nodes in the given tree.
# Space Complexity: O(H), where H is the height of the given tree.
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            flag = left + right
            if flag == 2:  # both children are covered
                flag = 1
            if left == -1 or right == -1:  # one side needs to be covered at least
                self.count += 1
                flag = 2
            return flag - 1

        if root and not root.left and not root.right:
            return 1
        self.count = 0
        temp = helper(root)
        return self.count + 1 if temp == -1 else self.count  # if root is not covered, add camera


# same idea, better implementation
def minCameraCover(self, root):
    self.res = 0

    def dfs(root):
        if not root:
            return 2
        l, r = dfs(root.left), dfs(root.right)
        if l == 0 or r == 0:
            self.res += 1
            return 1
        return 2 if l == 1 or r == 1 else 0

    return (dfs(root) == 0) + self.res


# readable codes
# https://leetcode.com/problems/binary-tree-cameras/solution/770395
# https://leetcode.com/problems/binary-tree-cameras/discuss/211966/Super-Clean-Java-solution-beat-100-DFS-O(n)-time-complexity

"""
class Solution {
    int camera = 0;
    public enum Camera { HAS_CAMERA, COVERED, PLEASE_COVER };
    
    public int minCameraCover(TreeNode root) {
        // If root is not covered then we need to place a camera at root node
        return cover(root) == Camera.PLEASE_COVER ? ++camera : camera;
    }
    
    public Camera cover(TreeNode root) {
        
        // Base case - if there is no node then it's already covered
        if (root == null)
            return Camera.COVERED;
        
        // Try to cover left and right children's subtree
        Camera l = cover(root.left);
        Camera r = cover(root.right);
        
        // If Any one of the children is not covered then we must place a camera at current node
        if (l ==  Camera.PLEASE_COVER || r == Camera.PLEASE_COVER) {
            camera++;
            return Camera.HAS_CAMERA;
        }
        
        // If any one of left or right node has Camera then the current node is also covered
        if (l== Camera.HAS_CAMERA || r == Camera.HAS_CAMERA) 
            return Camera.COVERED;
        
        // If None of the children is covering the current node then ask it's parent to cover
        return Camera.PLEASE_COVER;
    }
}
"""
