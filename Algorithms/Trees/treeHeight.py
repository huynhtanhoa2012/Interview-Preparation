def treeHeight(root):
    if not root:
        return -1
    
    return max(treeHeight(root.left), treeHeight(root.right)) + 1