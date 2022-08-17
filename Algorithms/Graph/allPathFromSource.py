def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    
    # edge cases:
    if not graph:
        return []

    # build di-graph:
    d = {}
    for i in range(graph):
        d[i] = graph[i]
    
    res = []
    n = len(graph) - 1
    stack = [(0,[0])]   # store node and path leading to node

    while stack:
        node, path = stack.pop()

        if node == n:
            res.append(path)
        
        # Traverse all neighbor nodes
        for neighbor in d[node]:
            stack.append((neighbor, [path] + neighbor ))
    
    return res

        





