class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sortedArrayToBST(nums: list[int]) -> TreeNode:

    def preorder(left, right) -> TreeNode:
        if left > right:
            return None
        # choose middle element, always left element
        mid = (left + right)//2
        # create root node, left and right node
        root = TreeNode(nums[mid])
        root.left = preorder(left, mid-1)
        root.right = preorder(mid+1, right)

        return root
    
    return preorder(0, len(nums)-1)

