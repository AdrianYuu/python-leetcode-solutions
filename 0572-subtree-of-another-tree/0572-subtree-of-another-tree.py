# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(r, s):
            # if both null
            if not r and not s:
                return True

            # if the current is the same we need
            # to check for the child too
            if r and s and r.val == s.val:
                return (
                    same_tree(r.left, s.left) and
                    same_tree(r.right, s.right)
                )

            return False

        # if the subRoot is null,
        # automatically it's a subtree of root
        if not subRoot:
            return True

        # if there are no root just return False
        if not root:
            return False

        # if it's the same tree just return True
        if same_tree(root, subRoot):
            return True
        
        # if the condition above is not fullfilled,
        # we need to check maybe the child contains the subtree
        # we use OR because only one needs to be True
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )