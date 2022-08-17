"""
Each time a recursive function calls itself, it reduces the given problem into subproblems.

1. A simple base case - a terminating point
2. Recurrence relation - A set of rules that reduces all other cases towards the base case.

When in doubt, write down the recurrence relationship.
Whenever possible, apply memoization.

----------------------------############################----------------------------
The difference between D&C and recursion is break down into 2 or more subproblem rather than 1

Divide and conquer
    1. Divide the problem S into a set of subproblems: {S_1, S_2, ... S_n}
    2. Conquer. Solve each subproblem recursively. 
    3. Combine. Combine the results of each subproblem.
"""