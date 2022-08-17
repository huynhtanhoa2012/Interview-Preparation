"""
Backtracking is an algorithm for finding all solutions 
by exploring all potential candidates.

If the solution candidate turns to be not a solution 
(or at least not the last one), 
backtracking algorithm discards it by making some changes 
on the previous step, backtracks and then try again.


"""

"""
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
"""

