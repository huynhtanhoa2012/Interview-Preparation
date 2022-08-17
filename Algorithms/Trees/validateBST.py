from cmath import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(root: TreeNode) -> bool:

        # Use valid Range (-inf, +inf)
        def validate(root, low, high) -> bool:
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return validate(root.left, low, root.val) and validate(root.right, root.val, high)
        
        # Use inorder Traversal
        def inorder(root) -> bool:
            if not root:
                return True
            # travel left
            if not inorder(root.left):
                return False
            # check root
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)
        self.prev = float("-inf")
        return inorder(root)