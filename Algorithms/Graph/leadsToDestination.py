def leadsToDestination(n: int, edges: list[list[int]], 
source: int, destination: int) -> bool:

    # Build di-graph:
    d = [[] for _ in range(n)]
    for u, v in edges:
        d[u].append(v)
    
    # Pre-processing
    visited = set([source])
    stack = [source]

    while stack:
        node = stack.pop()

        # 1. If leaf node check whether it is destination
        if len(d[node]) == 0 and node != destination:
            return False

        # 2. Check cycle in graph
        for neighbor in d[node]:
            if neighbor in visited: # and neighbor !=
                return False
            if neighbor != destination:
                stack.append(neighbor)
                visited.add(neighbor)
    return True

leadsToDestination(3,[[0,1],[0,2]],0,2) 