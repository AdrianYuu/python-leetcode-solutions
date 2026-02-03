# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            current_lvl = []

            for _ in range(len(q)):
                current = q.popleft()
                current_lvl.append(current.val)

                if current.left:
                    q.append(current.left)

                if current.right:
                    q.append(current.right)

            result.append(current_lvl)

        return result