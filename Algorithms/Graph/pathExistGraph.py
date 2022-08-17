import queue


def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:

    # Initialize list to store vertices
    adjacency_list = [[] for _ in range(n)]

    # add connections of vertices (undirected graph)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Initilize a stack
    stack = [source]
    visited = set([source])
    while stack:
        # Pop a vertex from stack to visit next
        current = stack.pop()

        if current == destination:
            return True
        
        # Push all the neighbours of v in stack that are not visited
        for vertex in adjacency_list[current]:
            if vertex not in visited:
                visited.add(vertex)
                stack.append(vertex)

    return False

# Breath First Search
def validPathBFS(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    
    # Preprocessing graph
    adjacency_list = [[] for _ in range(n)]

    for u,v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # BFS
    q = [source]
    visited = set([source])

    while q:
        current = q.pop(0)
        if current == destination:
            return True
        # Visited all neighbors
        for vertex in adjacency_list[current]:
            if vertex not in visited:
                visited.add(vertex)
                q.append(vertex)
    
    return False




validPath(3, [[0,1],[1,2],[2,0]], 0, 2)