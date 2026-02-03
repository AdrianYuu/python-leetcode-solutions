# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(root, max):
            if not root:
                return
    
            if root.val >= max:
                max = root.val
                nonlocal result
                result += 1

            left = dfs(root.left, max)
            right = dfs(root.right, max)

        dfs(root, root.val)

        return result