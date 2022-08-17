def leafSum(node):
    total = 0
    def isLeaf(node):
        return node.getChildNodes.size() == 0
        
    if not node:
        return 0
    if isLeaf(node):
        return node.value()
    for child in node.getChildNodes():
        total += leafSum(child)
    return total
    