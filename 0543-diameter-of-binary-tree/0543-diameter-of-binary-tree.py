# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def bfs(root):
            if not root:
                return 0

            left = bfs(root.left)
            right = bfs(root.right)

            nonlocal result
            result = max(result, left + right)

            return max(left, right) + 1

        bfs(root)

        return result