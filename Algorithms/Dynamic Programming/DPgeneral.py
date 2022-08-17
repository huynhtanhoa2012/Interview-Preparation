"""
How to Identify if it is a DP problem or not:
    + Build recursive solution and Identify the base cases. 
    + If smaller problems are called multiple times during recursion 
    then the given problem can be solved by using dynamic programming.

The first characteristic that is common in DP problems is 
that the problem will ask for the optimum value (maximum or minimum) of something, 
or the number of ways there are to do something. For example:
    + What is the minimum cost of doing...
    + What is the maximum profit from...
    + How many ways are there to do...
    + What is the longest possible...
    + Is it possible to reach a certain point...

The second characteristic that is common in DP problems is 
    + that future "decisions" depend on earlier decisions. Deciding to do 
    something at one step may affect the ability to do something in a later step

Decide if you want to implement it using Top down or bottom up approach:
    + We recommend to compare the properties of both the approaches 
    and undestand pros and cons of each. 

Top-down: 
    where we are storing the solution of sub-problems in an extra memory 
    or look-up table to avoid the recomputation.

Bottom-up: 
    This is an iterative approach to build the solution of the sub-problems 
    and store the solution in an extra memory.


"""