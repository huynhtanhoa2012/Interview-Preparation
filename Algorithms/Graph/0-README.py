""" --------------Depth First Search----------------
DFS-iterative (G, s): 
    let S be stack
    S.push( s )        
    mark s as visited.

    while ( S is not empty):
        v  =  S.pop( )
        //Push all the neighbours of v in stack that are not visited   
        for all neighbours w of v in Graph G:
            if w is not visited :
                S.push( w )         
                mark w as visited

DFS-recursive(G, s):
        mark s as visited
        for all neighbours w of s in Graph G:
            if w is not visited:
                DFS-recursive(G, w)
"""

""" --------------Single Source Shortest Path----------------
Dijkstra's algorithm” solves the “single-source shortest path” problem 
in a weighted directed graph with non-negative weights.


"""

