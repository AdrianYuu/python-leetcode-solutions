# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            result.append(q[-1].val)

            for _ in range(len(q)):
                current = q.popleft()

                if current.left:
                    q.append(current.left)
                
                if current.right:
                    q.append(current.right)

        return result