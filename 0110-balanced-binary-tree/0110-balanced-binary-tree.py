# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        def bfs(root):
            if not root:
                return 0

            left = bfs(root.left)
            right = bfs(root.right)

            nonlocal result
            if abs(right - left) > 1:
                result = False
                return 0

            return max(left, right) + 1

        bfs(root)

        return result