"""
----------------------------HEAP SORT-----------------------------------
1. Heapify all elements into a Min Heap.
2. Record and delete the top element.
3. Put the top element into an array T that stores all sorted elements. 
Now, the Heap will remain a Min Heap.
4. Repeat steps 2 and 3 until the Heap is empty. 
The array T will contain all elements sorted in ascending order.

Time complexity: O(NlogN)
Space complexity: O(N)
"""

"""
----------------------------The Top K Problem-----------------------------------
APPROACH 1
1. Construct a Max Heap.
2. Add all elements into the Max Heap.
3. Traversing and deleting the top element (using pop() or poll() for instance), 
and store the value into the result array T.
4. Repeat step 3 until we have removed the K largest elements.

Time complexity: O(KlogN+N)
Space complexity: O(N)
"""
